# Quick Reference - Learning Notes

## Cheat Sheet / Referencia Rápida

### SOLID Principles

**When**: Diseñando código mantenible / Cuando diseñes código

- **SRP**: Una responsabilidad por tipo
- **OCP**: Extensión sin modificación (interfaces)
- **LSP**: Implementaciones intercambiables
- **ISP**: Interfaces pequeñas y enfocadas
- **DIP**: Inyectar abstracciones, no concretos

### ACID vs BASE

**When**: Eligiendo base de datos / Cuando elijas BD

```text
ACID  ← Consistencia, transacciones, lento, vertical
BASE  ← Disponibilidad, eventual, rápido, horizontal
```

### PACELC Theorem

**When**: Diseñando sistema distribuido / Cuando diseñes distribuido

```text
Partición: Elige A (disponible) o C (consistente)
Normal: Elige L (latencia) o C (consistencia)
```

### Exponential Backoff

**When**: Reintentando en fallos transitorios / En reintentos

```text
delay = base × (multiplier ^ attempt)
+ jitter para prevenir manada atronadora
```

### Backpressure

**When**: Productor rápido, consumidor lento / Mismatch de velocidad

```text
Canal bufferizado lleno → Productor se bloquea → Auto-throttle
```

### Service Discovery

**When**: Microservicios necesitan localizarse / En microservicios

```text
Cliente-lado: Clientes consultan registro
Servidor-lado: Load balancer consulta (simpler clients)
```

### Saga Pattern

**When**: Transacción distribuida sin ACID / En transacciones distribuidas

```text
Coreografía: Eventos, descentralizado, estado difícil de rastrear
Orquestación: Coordinador central, estado claro, bottleneck potencial
```

### REST API Gin

**When**: Construyendo API HTTP / Cuando construyas API REST

```text
GET /users/:id          → Obtener
POST /users             → Crear (201)
PUT /users/:id          → Actualizar
DELETE /users/:id       → Eliminar
```

### Test Patterns

**When**: Escribiendo pruebas / En testing

```text
Unit (80%)        - Fast, mocks
Integration (15%) - Realistic, fakes
E2E (5%)         - Slow, actual interfaces
```

### Functional Options

**When**: Configurando objetos complejos con defaults / En constructores

```text
NewServer(WithPort(8080), WithTimeout(30s))
```

### 12-Factor App

**When**: Construyendo SaaS/Cloud Native Apps / Arquitectura

```text
Codebase, Dependencies, Config, Backing Services
Build/Release/Run, Processes, Port Binding, Concurrency
Disposability, Dev/Prod Parity, Logs, Admin Proc
```

---

## Decision Trees / Árboles de Decisión

### "¿Qué patrón de saga?"

```text
¿Flujo simple?
├─ Sí → Coreografía (event-driven)
└─ No → Orquestación (central coordinator)
```

### "¿Qué database approach?"

```text
¿Prioridad: Exactitud?
├─ Sí → ACID (transacciones, consistencia)
└─ No → BASE (disponibilidad, velocidad)
```

### "¿Cuántos tests?"

```text
├─ 80% unit tests (rápidas)
├─ 15% integration (realistas)
└─ 5% E2E (críticas)
```

### "¿Service discovery?"

```text
¿Control fino, infraestructura custom?
├─ Sí → Client-side
└─ No → Server-side (cloud-native)
```

---

## Files at a Glance

### English (EN)

| Archivo | Propósito | Complejidad |
|---------|-----------|------------|
| SOLID_PRINCIPLES | 5 principios diseño | Media |
| ACID_VS_BASE | Trade-offs BD | Baja |
| PACELC_THEOREM | Sistemas distribuidos | Alta |
| EXPONENTIAL_BACKOFF | Reintentos resilientes | Media |
| BACKPRESSURE | Control de flujo | Media |
| SERVICE_DISCOVERY | Microservicios ubicación | Media |
| SAGA_PATTERNS | Transacciones distribuidas | Alta |
| REST_API_GIN | APIs REST | Baja |
| TEST_PATTERNS | Estrategias testing | Media |
| FUNCTIONAL_OPTIONS | Configuración flexible | Media |
| APP_12_FACTOR | Arquitectura Cloud Native | Baja |

### Spanish (ES)

Mismos nombres + _ES.md suffix

---

## 80/20 Learning Path

**Si tienes 1 hora**, lee en orden:

1. SOLID_PRINCIPLES (15 min)
2. ACID_VS_BASE (10 min)
3. EXPONENTIAL_BACKOFF (10 min)
4. BACKPRESSURE (10 min)
5. REST_API_GIN (15 min)

**Si tienes 1 semana**:
Leer todos los EN en orden: Beginner → Intermediate → Advanced

**Si tienes 1 mes**:

- Inglés: Lee todos
- Español: Lee los que use frecuentemente
- Práctica: Implementa patrones en proyectos

---

## Common Mistakes

| Patrón | Evitar |
|--------|--------|
| SOLID | Over-engineering trivial código |
| ACID vs BASE | Forzar ACID en todos lados |
| PACELC | Ignorar retraso en operación normal |
| Backoff | Sin jitter → reintento sincronizado |
| Backpressure | Buffer demasiado grande |
| Service Discovery | Sin health checks |
| Saga | Sin transacciones compensatorias |
| Tests | Demasiados E2E, pocos unit |
| 12-Factor | Hardcodear config o guardar estado local |

---

Última actualización: Octubre 16, 2025
