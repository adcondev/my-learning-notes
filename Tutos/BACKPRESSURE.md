# Backpressure in Go

Backpressure prevents a fast producer from overwhelming a slow consumer by controlling data flow. In Go, use buffered channels and `select` to signal or block when buffers fill, forcing the producer to wait.

## Key Concepts

- **Producer**: Sends data to a channel
- **Consumer**: Reads from the channel
- **Backpressure**: Occurs when channel buffer fills; sender blocks, slowing production
- **Buffered Channels**: Channels with capacity that buffer values before blocking
- **Select with Default**: Non-blocking channel operations to handle backpressure

## How It Works

```
Fast Producer → [Buffer: capacity=3] → Slow Consumer
                        ↑
                   When full: Producer blocks
                   Forces producer to wait
                   System reaches equilibrium
```

When a producer tries to send on a full channel:
- Send operation blocks
- Producer stops generating
- This natural throttling prevents memory overflow
- System reaches equilibrium based on consumer speed

## Pattern: Select with Default Case

```go
select {
case ch <- value:      // Non-blocking send
    // Success
default:               // Executes if send would block
    // Handle backpressure: retry, wait, drop, or aggregate
}
```

## Pattern: Buffered Channel Sizing

- **Buffer size = 0** (unbuffered): Sender blocks until receiver ready
- **Buffer size = 1-10**: Small buffer, quick backpressure signal
- **Buffer size = large**: High buffering, delayed backpressure signal

Choosing buffer size determines how much "lag" the system tolerates before applying backpressure.

## Backpressure Propagation

```
Service A → Channel (size=5) → Service B
  ↓                              ↓
[Fast]                      [Slow - 2 msgs/sec]

Timeline:
- Seconds 1-2: Buffer fills (5 messages queued)
- Second 3: Service A blocks on send (backpressure applies)
- Service A stops producing until B consumes some
- System auto-throttles to B's speed
```

## Real-world Scenario

Without backpressure: High-frequency events flood a slow processor, causing memory exhaustion and crash.

With backpressure: Event producer automatically slows down when processor can't keep up. System remains stable even under pressure.

## Explanation

Backpressure is Go's elegant solution to the producer-consumer mismatch. By using buffered channels with limited capacity, slow consumers naturally throttle fast producers without explicit congestion management. The channel buffer acts as a shock absorber—when full, the producer blocks, preventing memory overflow.

This is especially powerful in microservices: when downstream service is overloaded, upstream automatically backs off instead of queuing infinite messages. The result is graceful degradation rather than cascade failure.

The key insight: buffered channels create implicit flow control. No need for complex congestion algorithms—the language primitive handles it naturally.