# Saga Pattern in Microservices

The Saga pattern maintains data consistency across multiple services in distributed transactions without tight coupling. It breaks distributed transactions into sequences of local transactions with compensating actions for failures.

## Key Concepts

- **Distributed Transaction**: Operation spanning multiple services that must all succeed or all be compensated
- **Local Transaction**: Operation within a single service
- **Compensating Transaction**: Reverses effects of a successful transaction (undo operation)
- **Choreography**: Services react to events independently
- **Orchestration**: Central coordinator manages the flow

## Two Approaches

### Choreography: Event-Driven

```
Order Service          Payment Service       Inventory Service     Shipping Service
      │                      │                      │                     │
      ├─ OrderCreated ───────→│                      │                     │
      │  (publish)            │                      │                     │
      │                       ├─ PaymentProcessed ──→│                     │
      │                       │  (publish)           │                     │
      │                       │                      ├─ ItemsReserved ────→│
      │                       │                      │  (publish)          │
      │                       │                      │                     │
      │                       │                      │← DeliveryScheduled ─┤
      │                       │                      │  (publish)          │
```

**Decentralized**: No coordinator
**Loose Coupling**: Services communicate via events
**Trade-off**: Hard to track overall state

### Orchestration: Coordinated

```
                    Saga Orchestrator
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    Order Service    Payment Service    Inventory Service
         │                 │                 │
         ├─ Create ───────→│                 │
         │← OrderId ───────┤                 │
         │                 ├─ Process ──────→│
         │                 │← Confirmed ────┤
         │                 │                 ├─ Reserve ───→
         │                 │                 │← Reserved ──┤
         │                 │                 │              
```

**Centralized**: Orchestrator controls flow
**Clear Visibility**: State in one place
**Trade-off**: Orchestrator becomes bottleneck

## Choreography Pattern

```go
// Service reacts to events independently
type OrderService struct {
    bus EventBus
}

func (s *OrderService) CreateOrder(order Order) {
    // Local transaction
    saved := s.db.Save(order)
    
    // Publish event - others react
    s.bus.Publish("OrderCreated", order)
}

// Somewhere else: PaymentService listens
func (s *PaymentService) OnOrderCreated(order Order) {
    payment := s.process(order)
    
    if payment.Success {
        s.bus.Publish("PaymentProcessed", order)
    } else {
        s.bus.Publish("PaymentFailed", order)
    }
}

// And elsewhere: InventoryService handles failure
func (s *InventoryService) OnPaymentFailed(order Order) {
    s.release(order.ID) // Compensating transaction
    s.bus.Publish("OrderCompensated", order)
}
```

## Orchestration Pattern

```go
type OrderSaga struct {
    orderSvc   OrderService
    paymentSvc PaymentService
    inventorySvc InventoryService
}

func (s *OrderSaga) Execute(order Order) error {
    // Step 1: Create order
    created, err := s.orderSvc.Create(order)
    if err != nil {
        return err
    }
    
    // Step 2: Process payment
    payment, err := s.paymentSvc.Process(order)
    if err != nil {
        // Compensate: Cancel order
        s.orderSvc.Cancel(created.ID)
        return err
    }
    
    // Step 3: Reserve inventory
    reserved, err := s.inventorySvc.Reserve(order)
    if err != nil {
        // Compensate: Refund and cancel
        s.paymentSvc.Refund(payment.ID)
        s.orderSvc.Cancel(created.ID)
        return err
    }
    
    return nil
}
```

## Choreography vs Orchestration

| Aspect | Choreography | Orchestration |
|--------|-------------|---------------|
| **Complexity** | Distributed across services | Centralized in orchestrator |
| **Coupling** | Loose (event-based) | Tighter (direct calls) |
| **Visibility** | Hard to track | Clear state tracking |
| **Scalability** | Highly scalable | Potential bottleneck |
| **Failure Recovery** | Per-service compensation | Orchestrator-coordinated |
| **Testing** | Difficult (async events) | Easier (synchronous flow) |

## When to Use Each

### Choose Choreography When

- Services naturally react to events
- Business process is relatively simple
- Team values autonomy and loose coupling
- Event-driven architecture already exists

### Choose Orchestration When

- Complex transaction with many dependencies
- Need clear visibility into saga state
- Centralized error handling preferred
- Process flow changes frequently

## Implementation Patterns

### Compensating Transactions

Each forward operation must have an undo:

```
Create Order        → Failure → Cancel Order
Process Payment     → Failure → Refund
Reserve Inventory   → Failure → Release
```

### Idempotency

Operations must be safely retryable:

```go
// Idempotent: Creating same order twice returns same result
func (s *OrderService) Create(order Order) Order {
    if existing := s.db.FindByID(order.ID); existing != nil {
        return existing
    }
    return s.db.Save(order)
}
```

### Timeouts and Deadletter

Handle unresponsive services:

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

result, err := s.remoteService.Call(ctx, request)
if err == context.DeadlineExceeded {
    // Handle timeout: compensate or retry
}
```

## Explanation

The Saga pattern solves distributed transactions by replacing ACID guarantees with a series of compensating transactions. Instead of atomic "all or nothing," sagas ensure "success for all or undo all."

Choreography is more autonomous and scalable but harder to reason about—no central place showing the full transaction flow. Orchestration is opposite: easier to understand and debug, but the coordinator becomes critical infrastructure.

In practice, many systems use a hybrid approach: orchestration for critical paths (checkout, payment) and choreography for auxiliary tasks (notifications, analytics). This balances clarity with scalability.