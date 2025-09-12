# REST API with Gin in Go

Gin is a high-performance HTTP web framework for Go, ideal for building REST APIs with routing, middleware, and JSON handling.

## Key Concept

- **Routing**: Define endpoints with HTTP methods (e.g., POST).
- **JSON Binding**: Parse incoming JSON payloads into structs.
- **Response**: Return JSON responses using Gin's context methods.
- **Middleware**: Add features like logging or CORS.

## Simple Example

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type Request struct {
	Name string `json:"name"`
}

func main() {
	r := gin.Default()

	r.POST("/hello", func(c *gin.Context) {
		var req Request
		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		c.JSON(http.StatusOK, gin.H{"response": "Hello, " + req.Name})
	})

	r.Run(":8080") // Start server on port 8080
}
```

## Explanation

- **Struct for Request**: `Request` binds the incoming JSON field "name".
- **Binding**: `ShouldBindJSON` parses the JSON; errors if invalid.
- **Response**: Uses `c.JSON` to send "Hello, {Name}" back.
- **Use case**: Test with `curl -X POST http://localhost:8080/hello -H "Content-Type: application/json" -d '{"name":"YourName"}'`.
