# CAP Theorem in Distributed Systems

The CAP Theorem states that in a distributed system, you can only guarantee two out of three properties: Consistency, Availability, and Partition Tolerance. It's a fundamental trade-off when designing systems that handle data across multiple nodes.

## Key Concepts

- **Consistency**: All nodes see the same data at the same time (strong consistency ensures reads return the most recent write).
- **Availability**: The system remains operational and responds to requests, even during failures.
- **Partition Tolerance**: The system continues to function despite network partitions (e.g., nodes can't communicate).

## Simple Example

Consider a distributed database with two nodes (A and B). A partition occurs, splitting the network.

- **CA System** (prioritizes Consistency and Availability): If a write happens on node A, node B must wait for sync before responding, but if partition persists, availability drops.
- **CP System** (prioritizes Consistency and Partition Tolerance): Node B rejects reads/writes during partition to maintain consistency, sacrificing availability.
- **AP System** (prioritizes Availability and Partition Tolerance): Both nodes accept writes independently, leading to eventual consistency (data may differ temporarily).

```go
// Simplified Go simulation of CAP trade-off
package main

import (
    "fmt"
    "sync"
    "time"
)

// Simulate nodes with a shared channel for communication
func node(name string, ch chan string, wg *sync.WaitGroup) {
    defer wg.Done()
    for msg := range ch {
        fmt.Printf("%s received: %s\n", name, msg)
        // Simulate processing delay
        time.Sleep(100 * time.Millisecond)
    }
}

func main() {
    ch := make(chan string, 10) // Buffered channel simulates network
    var wg sync.WaitGroup

    wg.Add(2)
    go node("Node A", ch, &wg)
    go node("Node B", ch, &wg)

    // Simulate writes (partition by closing channel briefly)
    ch <- "Write 1"
    close(ch) // Simulate partition: no more communication
    ch = make(chan string, 10) // Reopen for availability demo

    wg.Wait()
    fmt.Println("Partition handled: Availability prioritized, but consistency may lag.")
}
```

## Explanation

- **Trade-off**: During partitions, you must choose between consistency (wait for sync) or availability (serve stale data). No system achieves all three simultaneously.
- **Real-world Examples**:
  - **CP**: Traditional RDBMS like PostgreSQL (consistency over availability).
  - **AP**: NoSQL like Cassandra (availability and partition tolerance, with eventual consistency).
  - **CA**: Rare in practice; assumes no partitions (e.g., single-node systems).
- **Implications**: Design for your use case—e.g., banking needs consistency, social media favors availability.
- **Best Practice**: Use strategies like quorum reads/writes or CRDTs to balance CAP properties