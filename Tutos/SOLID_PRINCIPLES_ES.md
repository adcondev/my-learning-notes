# Principios SOLID en Go

SOLID representa cinco principios de diseño que permiten código mantenible, escalable y verificable. Las interfaces implícitas y composición de Go se alinean naturalmente con estos principios, haciendo SOLID una guía práctica más que reglas estrictas.

## Conceptos Clave

- **Responsabilidad Única (SRP)**: Cada tipo tiene una única razón para cambiar
- **Abierto/Cerrado (OCP)**: Abierto para extensión, cerrado para modificación
- **Sustitución de Liskov (LSP)**: Las implementaciones son intercambiables sin romper contratos
- **Segregación de Interfaces (ISP)**: Los clientes no deben depender de interfaces que no usan
- **Inversión de Dependencias (DIP)**: Depender de abstracciones, no de tipos concretos

## 1. Principio de Responsabilidad Única

Cada struct debe tener exactamente una razón para cambiar. En Go, esto significa separar responsabilidades en tipos distintos.

### El Problema

Un tipo `User` que hace validación, persistencia, envío de emails y formateo. Cada cambio en cualquiera de estas áreas modifica el mismo tipo. Difícil de probar, alta acoplamiento.

### La Solución

Separar en `UserValidator`, `UserRepository`, `EmailService`, `UserFormatter`. Cada tipo tiene una única razón para cambiar. Fácil de probar, componentes independientes.

**Trade-off**: Más archivos/tipos, pero cada uno más simple.

## 2. Principio Abierto/Cerrado

El software debe estar abierto para extensión sin modificar código existente. Usar interfaces para agregar comportamiento.

### El Problema

Función `ProcessPayment` con switch de métodos de pago. Cada nuevo método requiere modificar la función, arriesgando funcionalidad existente.

### La Solución

Interfaz `PaymentProcessor`. Cada método de pago es una implementación. Nuevos métodos se agregan sin modificar código existente.

```
PaymentProcessor (interfaz)
├── CreditCard
├── PayPal
└── Cryptocurrency (nuevo, sin modificar existentes)
```

**Trade-off**: Requiere diseñar pensando en extensibilidad, pero permite agregar funcionalidad con seguridad.

## 3. Principio de Sustitución de Liskov

Todas las implementaciones de una interfaz deben ser intercambiables sin romper el programa. El contrato debe honrarse.

### El Problema

Interfaz `Bird` con método `Fly()`. `Eagle` vuela correctamente, pero `Penguin` lanza error. Viola el contrato, causa panics en tiempo de ejecución.

### La Solución

Interfaces separadas: `Bird` (base), `FlyingBird`, `SwimmingBird`. `Eagle` implementa `FlyingBird`, `Penguin` implementa `SwimmingBird`. El sistema de tipos previene usos incorrectos.

**Trade-off**: El compilador atrapa violaciones, previene bugs sutiles en runtime.

## 4. Principio de Segregación de Interfaces

Los clientes no deben depender de interfaces que no usan. Preferir muchas interfaces pequeñas sobre pocas grandes.

### El Problema

Interfaz `Worker` gigante: `Work()`, `Eat()`, `Sleep()`, `TakeMedicalLeave()`, `GetSalary()`. `Robot` debe implementar métodos irrelevantes (comer, dormir, vacaciones).

### La Solución

Interfaces pequeñas: `Workable`, `Eatable`, `Payable`. `Human` implementa todas, `Robot` solo `Workable`. Composición flexible.

**Patrón**: La librería estándar de Go ejemplifica esto (`io.Reader`, `io.Writer`, etc.).

## 5. Principio de Inversión de Dependencias

Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.

### El Problema

`UserService` depende directamente de `MySQLDB`. Cambiar base de datos requiere modificar `UserService`. Difícil probar con mock.

### La Solución

`UserService` depende de interfaz `Database`. Constructor inyecta `Database` concreto. Funciona con `MySQLDB`, `PostgresDB`, `MockDB`.

```go
service := NewUserService(&MySQLDB{})       // Producción
service := NewUserService(&PostgresDB{})    // Alternativo
service := NewUserService(&MockDB{})        // Testing
```

**Patrón**: Inyección en constructor es estándar en Go.

## Los 5 Principios de Un Vistazo

```
SRP  → Una responsabilidad por tipo
OCP  → Extender por interfaces, no modificación
LSP  → Implementaciones honran contratos
ISP  → Interfaces pequeñas y enfocadas
DIP  → Inyectar abstracciones, no tipos concretos
```

## Trade-offs y Aplicabilidad

| Principio | Costo | Beneficio | Cuándo Aplicar |
|-----------|-------|-----------|----------------|
| **SRP** | Más archivos/tipos | Fácil probar y modificar | Siempre |
| **OCP** | Requiere diseño | Extensiones seguras | Puntos de cambio anticipados |
| **LSP** | Diseño cuidadoso | Comportamiento predecible | Interfaces públicas |
| **ISP** | Proliferación de interfaces | Composición flexible | Múltiples implementaciones |
| **DIP** | Complejidad en constructor | Testeabilidad, desacoplamiento | Código de capa de servicios |

## Patrones Específicos de Go

- **Interfaces Implícitas**: Duck typing hace ISP natural (`io.Reader`, `io.Writer`)
- **Composición sobre Herencia**: Sin herencia, SRP es el default
- **Embedding de Structs**: Habilita OCP por composición
- **Funciones Constructoras**: Patrón estándar para DIP (`NewService(dep)`)
- **Tests Orientados a Tabla**: SRP hace esto natural

## Errores Comunes

- Over-engineering: Aplicar SOLID a código trivial
- Ignorar LSP: Implementaciones que violan contratos
- Interfaces Grasas: Crear interfaces catch-all
- Dependencias Circulares: Implementación incorrecta de DIP
- Generalización Prematura: Extraer abstracciones antes de que emerjan patrones

## Mejores Prácticas

1. **Comenzar Concreto**: Escribir código funcional, extraer interfaces cuando emergen patrones
2. **Aceptar Interfaces, Retornar Structs**: Llamador provee abstracción, función retorna tipo concreto
3. **Interfaces Mínimas**: Una o dos métodos por interfaz
4. **Diseño Orientado a Pruebas**: Principios SOLID emergen naturalmente de código verificable
5. **Refactorizar Incrementalmente**: Aplicar principios conforme crece la complejidad

## Explicación

Los principios SOLID en Go emergen naturalmente de la filosofía de Go: composición sobre herencia, interfaces implícitas, diseño simple y explícito. A diferencia de lenguajes que requieren diseño cuidadoso de jerarquías OOP, Go incentiva descubrir abstracciones por medio de implementaciones concretas.

Comenzar con código directo. Cuando notes duplicación o múltiples razones para cambiar un tipo, extrae responsabilidades. Cuando necesites variantes, define una interfaz. Cuando probar sea difícil, inyecta dependencias. Este enfoque bottom-up produce diseños más limpios que imponer SOLID top-down.

La librería estándar de Go (`io`, `net`, `encoding`) demuestra SOLID en la práctica. Estudia estos paquetes para entender cómo interfaces pequeñas y enfocadas, junto con composición, crean sistemas flexibles y mantenibles sin la sobrecarga de frameworks OOP empresariales.
