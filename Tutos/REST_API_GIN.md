# REST API with Gin in Go

Gin is a high-performance HTTP web framework for Go, ideal for building REST APIs with minimal boilerplate. It provides routing, middleware, JSON binding, and error handling out of the box.

## Key Concepts

- **Router**: Maps HTTP methods (GET, POST, PUT, DELETE) to handlers
- **Binding**: Automatic JSON parsing and validation from request body
- **Status Codes**: HTTP codes returned (200, 201, 400, 404, 500)
- **Middleware**: Functions that run before/after handlers (logging, auth, CORS)
- **Error Handling**: Structured error responses to clients

## Basic Structure

```go
// Create router
router := gin.Default() // Includes Logger and Recovery middleware

// Define route with handler function
router.GET("/users/:id", getUserHandler)   // GET /users/123
router.POST("/users", createUserHandler)   // POST /users
router.PUT("/users/:id", updateUserHandler) // PUT /users/123
router.DELETE("/users/:id", deleteUserHandler) // DELETE /users/123

// Start server
router.Run(":8080")
```

## Route Patterns

| Pattern | Meaning | Example Match |
|---------|---------|---------------|
| `/users` | Exact path | `/users` |
| `/users/:id` | Path parameter | `/users/123` |
| `/users/:id/posts` | Nested parameter | `/users/123/posts` |
| `/users/*action` | Wildcard | `/users/list`, `/users/search` |

## Handler Function Pattern

```go
func handleRequest(c *gin.Context) {
    // Get data from request
    id := c.Param("id")           // Path parameter
    name := c.Query("name")       // Query string
    
    // Parse JSON body
    var data RequestBody
    if err := c.ShouldBindJSON(&data); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    // Process
    result := processData(data)
    
    // Return response
    c.JSON(http.StatusOK, result)
}
```

## HTTP Status Codes

- **200 OK**: Request succeeded
- **201 Created**: Resource created
- **204 No Content**: Success, no body
- **400 Bad Request**: Invalid input
- **404 Not Found**: Resource doesn't exist
- **500 Internal Server Error**: Server failure

## Middleware Pattern

```go
// Logging middleware
router.Use(gin.Logger())

// Authorization middleware
router.Use(func(c *gin.Context) {
    token := c.GetHeader("Authorization")
    if token == "" {
        c.AbortWithStatusJSON(401, gin.H{"error": "unauthorized"})
        return
    }
    c.Next() // Continue to next handler
})

// Route group with specific middleware
authorized := router.Group("/api/admin")
authorized.Use(authMiddleware)
{
    authorized.GET("/stats", getStats)
    authorized.POST("/users", createUser)
}
```

## Testing API

```bash
# GET request
curl http://localhost:8080/users

# GET with parameter
curl http://localhost:8080/users/123

# POST with JSON body
curl -X POST http://localhost:8080/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice", "email":"alice@example.com"}'

# PUT request
curl -X PUT http://localhost:8080/users/123 \
  -H "Content-Type: application/json" \
  -d '{"name":"Bob"}'

# DELETE request
curl -X DELETE http://localhost:8080/users/123
```

## Key Features

- **No Middleware by Default**: Only Logger and Recovery when using `gin.Default()`
- **Request Context**: `*gin.Context` provides access to request/response data
- **Error Handling**: `c.JSON()` for responses, `c.AbortWithStatusJSON()` for errors
- **Binding Tags**: `json:"field" binding:"required,email"` for validation
- **Flexible Groups**: Organize routes with `router.Group()` for versioning

## Explanation

Gin excels at providing just enough abstraction for REST APIs without the overhead of full web frameworks. The context object `*gin.Context` centralizes request/response handling, middleware can be composed flexibly, and the binding system reduces boilerplate for validation.

Key insight: Status codes matter. Always return appropriate codes (201 for creates, 404 for missing resources). This helps clients and debugging tools understand what happened instantly. Consistent error format (JSON with "error" field) makes client-side error handling predictable.
