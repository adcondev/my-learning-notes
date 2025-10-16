# API REST con Gin en Go

Gin es un framework web HTTP de alto rendimiento para Go, ideal para construir APIs REST con mínimo código repetitivo. Proporciona routing, middleware, binding JSON, y manejo de errores lista para usar.

## Conceptos Clave

- **Router**: Mapea métodos HTTP (GET, POST, PUT, DELETE) a handlers
- **Binding**: Parsing y validación automática de JSON desde cuerpo de solicitud
- **Códigos de Estado**: Códigos HTTP retornados (200, 201, 400, 404, 500)
- **Middleware**: Funciones que se ejecutan antes/después de handlers (logging, auth, CORS)
- **Manejo de Errores**: Respuestas de error estructuradas al cliente

## Estructura Básica

```go
// Crear router
router := gin.Default() // Incluye middleware Logger y Recovery

// Definir ruta con función handler
router.GET("/users/:id", handleGetUser)
router.POST("/users", handleCreateUser)
router.PUT("/users/:id", handleUpdateUser)
router.DELETE("/users/:id", handleDeleteUser)

// Iniciar servidor
router.Run(":8080")
```

## Patrones de Rutas

| Patrón | Significado | Coincide con |
|--------|-----------|-------------|
| `/users` | Ruta exacta | `/users` |
| `/users/:id` | Parámetro de ruta | `/users/123` |
| `/users/:id/posts` | Parámetro anidado | `/users/123/posts` |
| `/users/*action` | Comodín | `/users/list`, `/users/search` |

## Patrón de Función Handler

```
func handleRequest(c *gin.Context) {
    // Obtener datos de solicitud
    id := c.Param("id")              // Parámetro de ruta
    name := c.Query("name")          // Query string
    
    // Parsear cuerpo JSON
    var data RequestBody
    if err := c.ShouldBindJSON(&data); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    
    // Procesar
    result := processData(data)
    
    // Retornar respuesta
    c.JSON(http.StatusOK, result)
}
```

## Códigos de Estado HTTP

- **200 OK**: Solicitud exitosa
- **201 Creado**: Recurso creado
- **204 Sin Contenido**: Éxito, sin cuerpo
- **400 Solicitud Inválida**: Entrada inválida
- **404 No Encontrado**: Recurso no existe
- **500 Error del Servidor**: Fallo del servidor

## Patrón de Middleware

```
// Middleware de logging
router.Use(gin.Logger())

// Middleware de autorización
router.Use(func(c *gin.Context) {
    token := c.GetHeader("Authorization")
    if token == "" {
        c.AbortWithStatusJSON(401, gin.H{"error": "unauthorized"})
        return
    }
    c.Next() // Continuar al próximo handler
})

// Grupo de rutas con middleware específico
authorized := router.Group("/api/admin")
authorized.Use(authMiddleware)
{
    authorized.GET("/stats", getStats)
    authorized.POST("/users", createUser)
}
```

## Pruebas de API

```bash
# Solicitud GET
curl http://localhost:8080/users

# GET con parámetro
curl http://localhost:8080/users/123

# POST con cuerpo JSON
curl -X POST http://localhost:8080/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice", "email":"alice@example.com"}'

# Solicitud PUT
curl -X PUT http://localhost:8080/users/123 \
  -H "Content-Type: application/json" \
  -d '{"name":"Bob"}'

# Solicitud DELETE
curl -X DELETE http://localhost:8080/users/123
```

## Características Clave

- **Sin Middleware por Defecto**: Solo Logger y Recovery cuando usas `gin.Default()`
- **Contexto de Solicitud**: `*gin.Context` proporciona acceso a datos de solicitud/respuesta
- **Manejo de Errores**: `c.JSON()` para respuestas, `c.AbortWithStatusJSON()` para errores
- **Tags de Binding**: `json:"field" binding:"required,email"` para validación
- **Grupos Flexibles**: Organizar rutas con `router.Group()` para versionado

## Explicación

Gin destaca en proporcionar exactamente la abstracción suficiente para APIs REST sin la sobrecarga de frameworks web completos. El objeto contexto `*gin.Context` centraliza el manejo de solicitud/respuesta, el middleware puede ser compuesto flexiblemente, y el sistema de binding reduce código repetitivo para validación.

Idea clave: Los códigos de estado importan. Siempre retorna códigos apropiados (201 para creaciones, 404 para recursos faltantes). Esto ayuda a clientes y herramientas de debugging a entender qué sucedió instantáneamente. Formato de error consistente (JSON con campo "error") hace el manejo de errores del lado del cliente predecible.
