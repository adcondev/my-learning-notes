# Service Discovery in Microservices

Service discovery manages and exposes service locations, enabling microservices to locate and communicate with each other dynamically. It decouples service location from hardcoded addresses, enabling auto-scaling and resilience.

## Key Concepts

- **Service Registry**: Centralized catalog of available service instances and their addresses
- **Registration**: Service registers itself on startup, deregisters on shutdown
- **Health Checks**: Periodic probes to detect and remove unhealthy instances
- **Client-side Discovery**: Clients query registry to find services
- **Server-side Discovery**: Load balancer queries registry internally

## Two Approaches

### Client-side Discovery

```
Client                Registry            Service A
  │                     │                    │
  ├─ Query for "api"───→│                    │
  │                     │← Returns instances │
  │                     │  [A1: host:8080,   │
  │                     │   A2: host:8081]   │
  │                                          │
  ├─ Choose A1 ────────────→ Request
  │                          Response ←─────┤
```

**Pros**: Direct connection, full control
**Cons**: Clients manage load balancing and failover

### Server-side Discovery

```
Client           Load Balancer        Registry        Service A
  │                   │                  │               │
  ├─ Request ───────→ │                  │               │
  │                   ├─ Query "api"────→│               │
  │                   │← Instance list    │               │
  │                   │                   │               │
  │                   ├─────────────────────→ Forward    │
  │                   │←───── Response ──────┤           │
  │← Response ────────┤                      │           │
```

**Pros**: Clients simplified, LB handles complexity
**Cons**: LB becomes potential bottleneck

## Service Registry Patterns

| Pattern | Tool | Use Case |
|---------|------|----------|
| **Consul** | Explicit registration | Microservices on VMs, self-managed K8s |
| **Kubernetes DNS** | Automatic (built-in) | Any containerized service |
| **Eureka** | Registration, heartbeat | Spring Boot, Netflix stack |
| **Cloud Vendor** | AWS/GCP/Azure | Cloud-native applications |

## Registration Pattern

```
Service starts
  │
  ├─ Register with registry
  │  [name: "user-service",
  │   address: "10.0.1.5",
  │   port: 8080,
  │   healthCheck: "GET /health"]
  │
  ├─ Periodic heartbeat (e.g., every 5s)
  │  "I'm still alive"
  │
  ├─ On failure or shutdown
  │  Deregister
  │
  └─ Registry removes stale entries
     after heartbeat timeout
```

## Health Checks

```
Registry          Service
  │                 │
  ├─ GET /health ───→│
  │                  │
  │← 200 OK ─────────┤ (Healthy: keep registered)
  
  ├─ GET /health ───→│
  │                  │
  │  (No response)   │ (Timeout: mark unhealthy)
  │
  └─ After N failures: Remove from registry
```

## Implementation Considerations

### What to Register

- Service name (unique identifier)
- Network address and port
- Version/tags for filtering
- Health check endpoint
- Metadata (region, canary flag, etc.)

### Health Check Strategies

- **Passive**: Clients report failures
- **Active**: Registry pings service
- **External**: Separate monitor checks
- **Application**: Service self-reports

## Comparison Matrix

| Aspect | Client-side | Server-side |
|--------|------------|------------|
| **Complexity** | High (clients) | Low (clients) |
| **Load Balancing** | Client library | Load balancer |
| **Latency** | Lower (direct) | Slightly higher |
| **Scalability** | Linear with clients | Bottleneck at LB |
| **Failure Handling** | Per client | Centralized |
| **Example** | Consul + client lib | Kubernetes |

## Explanation

Service discovery solves a fundamental problem in microservices: how do services find each other when locations change? Hardcoding addresses breaks auto-scaling and resilience; service discovery makes location a runtime concern.

The choice between client-side and server-side depends on your infrastructure:
- **Client-side** gives you fine-grained control and direct connections, ideal if you're managing your own infrastructure
- **Server-side** simplifies clients and centralizes complexity, ideal in cloud-native environments (Kubernetes, serverless)

Health checks prevent requests to dead services. Without them, clients repeatedly try failed instances. The registration/deregistration lifecycle ensures the registry stays accurate.

Modern platforms (Kubernetes, service meshes) automate much of this. Understanding the underlying patterns helps when building custom solutions or debugging issues.