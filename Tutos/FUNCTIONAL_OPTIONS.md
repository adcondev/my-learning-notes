# Functional Options Pattern in Go

The Functional Options pattern is a powerful way to design APIs in Go that require configuration. It allows you to create flexible, extensible, and clean APIs for your structs and functions.

## Prerequisites

- Basic understanding of Go structs and functions.
- Familiarity with variadic functions (`...Type`).
- Understanding of closures/anonymous functions.

## Key Concepts

- **Variadic Functions**: Functions that accept a variable number of arguments.
- **Higher-Order Functions**: Functions that return other functions.
- **Encapsulation**: Keeping configuration logic separate from business logic.
- **Default Values**: Handling optional parameters gracefully without nil checks or pointers.

## Visual Explanation

```mermaid
graph TD
    Client[Client Code] -->|Calls Constructor| NewServer[NewServer(...Options)]
    
    subgraph "Functional Options Pattern"
        NewServer -->|1. Init Default Config| Config[Default Config]
        NewServer -->|2. Apply Options| Apply[Loop through Options]
        
        Apply -->|Option 1| Opt1[WithPort(8080)]
        Apply -->|Option 2| Opt2[WithTimeout(5s)]
        
        Opt1 -->|Modifies| Config
        Opt2 -->|Modifies| Config
    end
    
    Config -->|3. Create Instance| Server[Server Instance]
    Server -->|Returns| Client
```

## Practical Implementation

Here is the canonical way to implement Functional Options in Go.

```go
package main

import "time"

// Server represents the complex object we want to configure
type Server struct {
    host    string
    port    int
    timeout time.Duration
}

// Option is a function type that modifies the Server
type Option func(*Server)

// NewServer creates a Server with default values and applies options
func NewServer(opts ...Option) *Server {
    // 1. Define defaults
    s := &Server{
        host:    "localhost",
        port:    80,
        timeout: 30 * time.Second,
    }

    // 2. Apply options
    for _, opt := range opts {
        opt(s)
    }

    return s
}

// WithPort returns an Option to set the port
func WithPort(port int) Option {
    return func(s *Server) {
        s.port = port
    }
}

// WithTimeout returns an Option to set the timeout
func WithTimeout(d time.Duration) Option {
    return func(s *Server) {
        s.timeout = d
    }
}

func main() {
    // Usage: Clean and expressive
    srv := NewServer(
        WithPort(8080),
        WithTimeout(5*time.Second),
    )
}
```

## Trade-offs

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Functional Options** | • Clean API<br>• Extensible (add new options without breaking changes)<br>• Safe defaults<br>• No nil checks needed | • More boilerplate code initially<br>• Slightly more complex to understand for beginners |
| **Config Struct** | • Simple to implement<br>• Grouped configuration | • Handling optional fields is messy (pointers or zero values)<br>• Breaking changes when adding fields |
| **Multiple Constructors** | • Simple for very few options | • Explodes with combinations (New, NewWithPort, NewWithTimeout...)<br>• Not idiomatic in Go |

## When to Use

- When your constructor has more than 3 parameters.
- When most parameters are optional.
- When you anticipate adding more configuration options in the future.
- When you want to provide a library with a stable API.

## Next Steps

- Explore the **Builder Pattern** for an object-oriented alternative (though less common in Go).
- Learn about **Fluent Interfaces** (method chaining), which is another way to handle configuration.

## Tags

#golang #design-patterns #api-design #clean-code #functional-programming
