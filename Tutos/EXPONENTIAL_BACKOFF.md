# Exponential Backoff in Go

Exponential backoff is a retry strategy that progressively increases wait time between retries to reduce system load. Essential for handling transient failures in distributed systems, especially when multiple clients retry simultaneously.

## Key Concepts

- **Initial Delay**: Starting wait time (e.g., 100ms)
- **Multiplier**: Exponential factor per retry (typically 2x)
- **Maximum Delay**: Cap to prevent waiting too long (e.g., 10s)
- **Jitter**: Random variation (±10-20%) to prevent synchronized retries
- **Maximum Retries**: Attempt limit (e.g., 5 tries)

## Why Exponential Backoff?

### The Problem: Thundering Herd

When multiple clients experience failure simultaneously and all retry immediately:
- Retry storm floods the system
- System already struggling can't recover
- Cascading failure occurs

### The Solution: Staggered Retries

```
Client 1: ===wait(100ms)=== retry ===wait(200ms)=== retry ===wait(400ms)===
Client 2: ===wait(120ms)=== retry ===wait(240ms)=== retry ===wait(480ms)===
Client 3: ===wait(140ms)=== retry ===wait(260ms)=== retry ===wait(420ms)===

Result: Retries spread out instead of synchronized.
System recovers, requests succeed.
```

## Delay Progression

```
Attempt 1: 100ms           (2^0 * 100ms)
Attempt 2: 200ms           (2^1 * 100ms)
Attempt 3: 400ms           (2^2 * 100ms)
Attempt 4: 800ms           (2^3 * 100ms)
Attempt 5: 1600ms → capped → 10s (max)

With jitter (±20%): Each actual delay varies randomly
around the exponential value
```

## Algorithm Structure

```go
for attempt := 0; attempt < maxRetries; attempt++ {
    try operation:
        if success: return
        
    calculate delay:
        exponential_delay = base_delay * (multiplier ^ attempt)
        delay = min(exponential_delay, max_delay)
        delay += random_jitter()
        
    wait(delay)
}
```

## Jitter: Why It Matters

Without jitter:
```
Multiple clients calculate same delay → synchronized retry → thundering herd
```

With jitter:
```
Multiple clients + randomness → staggered retries → system stabilizes
```

Typical jitter: ±10-20% of calculated delay

## Real-world Parameters

| Scenario | Base | Multiplier | Max | Retries | Jitter |
|----------|------|-----------|-----|---------|--------|
| **API Client** | 100ms | 2x | 10s | 5 | ±10% |
| **Database** | 50ms | 2x | 5s | 7 | ±15% |
| **Service Call** | 200ms | 2x | 30s | 4 | ±20% |
| **Batch Job** | 1s | 2x | 60s | 6 | ±5% |

## Explanation

Exponential backoff solves the retry problem in distributed systems by balancing two concerns:

1. **Recovery Time**: Early retries (small delays) recover quickly from brief outages
2. **System Load**: Later retries (large delays) prevent overwhelming a struggling system

The exponential curve allows rapid recovery from transient failures while protecting against cascading failures. Jitter, the seemingly minor detail, is crucial—it decorrelates retry attempts across clients, preventing the synchronized retry storms that can destroy a system during recovery.

This pattern is so fundamental that major cloud providers (AWS, Google Cloud, Azure) recommend it in their documentation. It's the canonical solution for resilient distributed systems.