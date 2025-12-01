# PACELC Theorem in Distributed Systems

The PACELC theorem extends CAP by addressing a critical limitation: what happens during normal operation when networks aren't partitioned? PACELC provides a complete design framework for both failure and normal conditions.

## Prerequisites

- Understanding of the **CAP Theorem** (Consistency, Availability, Partition Tolerance).
- Basic knowledge of database replication (synchronous vs. asynchronous).

## Key Concepts

- **P (Partition)**: Network failure between nodes.
- **A (Availability)**: System responds to requests.
- **C (Consistency)**: All nodes see the same data.
- **E (Else)**: Normal operation (no partition).
- **L (Latency)**: Response time.

## Visual Explanation

**"If Partition (P), choose A or C. Else (E), choose L or C."**

```mermaid
graph TD
    Start{Network State}
    
    Start -->|Partition (P)| P_Branch[Failure Mode]
    Start -->|Normal (E)| E_Branch[Normal Mode]
    
    P_Branch -->|Choose| PA[Availability (A)]
    P_Branch -->|Choose| PC[Consistency (C)]
    
    E_Branch -->|Choose| EL[Latency (L)]
    E_Branch -->|Choose| EC[Consistency (C)]
    
    PA --> Ex1[DynamoDB, Cassandra]
    PC --> Ex2[HBase, BigTable]
    EL --> Ex3[DynamoDB, Cassandra]
    EC --> Ex4[BigTable, HBase, RDBMS]
```

## Comparison Table

| System Type | During Partition | Normal Operation | Examples |
| :--- | :--- | :--- | :--- |
| **PA/EL** | Prefers Availability | Prefers Latency | Cassandra, DynamoDB |
| **PA/EC** | Prefers Availability | Prefers Consistency | MongoDB (default) |
| **PC/EL** | Prefers Consistency | Prefers Latency | BigTable, HBase |
| **PC/EC** | Prefers Consistency | Prefers Consistency | Traditional RDBMS (Postgres, MySQL) |

## Real-world Scenarios

### 1. Social Media Feed (PA/EL)
- **Goal**: User must always see *something*, even if slightly stale. Fast loading is critical.
- **Choice**: **PA** (Show old posts if network fails) / **EL** (Async replication for speed).

### 2. Banking Ledger (PC/EC)
- **Goal**: Account balance must be 100% accurate.
- **Choice**: **PC** (Reject transaction if network fails) / **EC** (Sync replication to ensure data safety).

## Trade-offs

- **Latency vs. Consistency**: In normal operation, you can't have both zero latency and perfect consistency. Sync replication (Consistency) adds latency. Async replication (Latency) risks data loss or staleness.
- **Availability vs. Consistency**: During partitions, you must choose between stalling (Consistency) or serving potentially wrong data (Availability).

## Next Steps

- Study **Quorum Consistency** (R + W > N) to tune these trade-offs dynamically.
- Learn about **Conflict Resolution** strategies (Last-Write-Wins, Vector Clocks) for PA/EL systems.

## Tags

#distributed-systems #cap-theorem #database-design #system-architecture #theory