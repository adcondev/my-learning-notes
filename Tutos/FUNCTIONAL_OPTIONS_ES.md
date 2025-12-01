# Patrón Functional Options en Go

El patrón Functional Options (Opciones Funcionales) es una forma poderosa de diseñar APIs en Go que requieren configuración. Te permite crear APIs flexibles, extensibles y limpias para tus structs y funciones.

## Prerrequisitos

- Entendimiento básico de structs y funciones en Go.
- Familiaridad con funciones variádicas (`...Type`).
- Entendimiento de closures/funciones anónimas.

## Conceptos Clave

- **Funciones Variádicas**: Funciones que aceptan un número variable de argumentos.
- **Funciones de Orden Superior**: Funciones que retornan otras funciones.
- **Encapsulamiento**: Mantener la lógica de configuración separada de la lógica de negocio.
- **Valores por Defecto**: Manejo elegante de parámetros opcionales sin necesidad de punteros o verificaciones de nil.

## Explicación Visual

```mermaid
graph TD
    Client[Código Cliente] -->|Llama Constructor| NewServer[NewServer(...Options)]
    
    subgraph "Patrón Functional Options"
        NewServer -->|1. Init Config Default| Config[Configuración Default]
        NewServer -->|2. Aplica Opciones| Apply[Iterar sobre Options]
        
        Apply -->|Opción 1| Opt1[WithPort(8080)]
        Apply -->|Opción 2| Opt2[WithTimeout(5s)]
        
        Opt1 -->|Modifica| Config
        Opt2 -->|Modifica| Config
    end
    
    Config -->|3. Crea Instancia| Server[Instancia del Server]
    Server -->|Retorna| Client
```

## Implementación Práctica

Aquí está la forma canónica de implementar Functional Options en Go.

```go
package main

import "time"

// Server representa el objeto complejo que queremos configurar
type Server struct {
    host    string
    port    int
    timeout time.Duration
}

// Option es un tipo de función que modifica el Server
type Option func(*Server)

// NewServer crea un Server con valores por defecto y aplica las opciones
func NewServer(opts ...Option) *Server {
    // 1. Definir defaults
    s := &Server{
        host:    "localhost",
        port:    80,
        timeout: 30 * time.Second,
    }

    // 2. Aplicar opciones
    for _, opt := range opts {
        opt(s)
    }

    return s
}

// WithPort retorna una Option para establecer el puerto
func WithPort(port int) Option {
    return func(s *Server) {
        s.port = port
    }
}

// WithTimeout retorna una Option para establecer el timeout
func WithTimeout(d time.Duration) Option {
    return func(s *Server) {
        s.timeout = d
    }
}

func main() {
    // Uso: Limpio y expresivo
    srv := NewServer(
        WithPort(8080),
        WithTimeout(5*time.Second),
    )
}
```

## Trade-offs (Ventajas y Desventajas)

| Enfoque | Pros | Contras |
| :--- | :--- | :--- |
| **Functional Options** | • API Limpia<br>• Extensible (añadir opciones no rompe código existente)<br>• Defaults seguros<br>• Sin validaciones de nil | • Más código boilerplate al inicio<br>• Ligeramente más complejo de entender para principiantes |
| **Config Struct** | • Simple de implementar<br>• Configuración agrupada | • Manejo sucio de campos opcionales (punteros o zero values)<br>• Cambios disruptivos al agregar campos requeridos |
| **Múltiples Constructores** | • Simple para muy pocas opciones | • Explosión combinatoria (New, NewWithPort, NewWithTimeout...)<br>• No es idiomático en Go |

## Cuándo Usar

- Cuando tu constructor tiene más de 3 parámetros.
- Cuando la mayoría de los parámetros son opcionales.
- Cuando anticipas agregar más opciones de configuración en el futuro.
- Cuando quieres proveer una librería con una API estable.

## Siguientes Pasos

- Explorar el **Builder Pattern** como una alternativa orientada a objetos (aunque menos común en Go).
- Aprender sobre **Fluent Interfaces** (encadenamiento de métodos), que es otra forma de manejar configuración.

## Etiquetas

#golang #design-patterns #api-design #clean-code #functional-programming
