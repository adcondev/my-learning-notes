# Service Discovery in Microservices

Service discovery manages and exposes service locations, enabling microservices to locate and communicate with each other dynamically. It handles registration, health checks, and lookup of service instances in distributed environments.

## Key Concepts

- **Service Registry**: Centralized database storing service instances, their locations, and metadata.
- **Service Registration**: Process where services register themselves upon startup and deregister on shutdown.
- **Health Checks**: Periodic verification of service availability to remove unhealthy instances.
- **Client-side Discovery**: Clients query the registry directly to find service locations.
- **Server-side Discovery**: Load balancer acts as intermediary, resolving service locations from the registry.

## Client-side vs Server-side Discovery

| Aspect | Client-side Discovery | Server-side Discovery |
|--------|----------------------|----------------------|
| **Architecture** | Clients connect directly to registry | Load balancer integrates with registry |
| **Client Responsibility** | Must implement registry client and load balancing | Only needs to know load balancer endpoint |
| **Load Balancing** | Client-side (e.g., round-robin in client library) | Server-side (handled by load balancer) |
| **Complexity** | Higher (clients manage discovery logic) | Lower (simplified client code) |
| **Performance** | Potentially faster (direct connections) | Slight overhead from load balancer |
| **Examples** | Eureka (Netflix), Consul client-side | Kubernetes services, AWS ALB with service discovery |

## Simple Example (Client-side with Go)

```go
package main

import (
    "fmt"
    "net/http"
    "time"
    
    "github.com/hashicorp/consul/api"
)

func registerService(client *api.Client, serviceID, serviceName, address string, port int) error {
    registration := &api.AgentServiceRegistration{
        ID:      serviceID,
        Name:    serviceName,
        Address: address,
        Port:    port,
        Check: &api.AgentServiceCheck{
            HTTP:     fmt.Sprintf("http://%s:%d/health", address, port),
            Interval: "10s",
            Timeout:  "5s",
        },
    }
    return client.Agent().ServiceRegister(registration)
}

func discoverService(client *api.Client, serviceName string) ([]*api.ServiceEntry, error) {
    return client.Health().Service(serviceName, "", true, nil)
}

func main() {
    config := api.DefaultConfig()
    config.Address = "localhost:8500" // Consul address
    client, err := api.NewClient(config)
    if err != nil {
        panic(err)
    }
    
    // Register service
    err = registerService(client, "user-service-1", "user-service", "localhost", 8080)
    if err != nil {
        panic(err)
    }
    
    // Discover service
    services, err := discoverService(client, "user-service")
    if err != nil {
        panic(err)
    }
    
    for _, service := range services {
        fmt.Printf("Found service: %s at %s:%d\n", service.Service.Service, service.Service.Address, service.Service.Port)
    }
    
    // Simulate running service
    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
    })
    http.ListenAndServe(":8080", nil)
}
```

## Explanation

- **Client-side Discovery**: Services register with a registry (e.g., Consul, Eureka). Clients query the registry to get service instances and handle load balancing themselves. This approach gives clients control but increases complexity.
- **Server-side Discovery**: Clients send requests to a load balancer, which queries the registry internally and routes traffic. This simplifies clients but introduces a potential bottleneck at the load balancer.
- **Differences**: The main distinction is the load balancer's role—client-side requires clients to manage discovery, while server-side delegates it. Both ensure dynamic service location but differ in where the discovery logic resides.
- **Use Cases**: Client-side for fine-grained control in custom architectures; server-side for simplicity in cloud-native environments with built-in load balancers.
- **Best Practices**: Implement health checks, use TTL for registrations, and consider caching to reduce registry load. Choose based on infrastructure—server-side fits Kubernetes, client-side suits custom setups.