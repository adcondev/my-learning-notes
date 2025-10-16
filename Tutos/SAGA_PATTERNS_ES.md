# Patrón Saga en Microservicios

El patrón Saga mantiene consistencia de datos entre múltiples servicios en transacciones distribuidas sin acoplamiento fuerte. Divide transacciones distribuidas en secuencias de transacciones locales con acciones compensatorias para fallos.

## Conceptos Clave

- **Transacción Distribuida**: Operación que abarca múltiples servicios que debe tener éxito en todos o deshacer en todos
- **Transacción Local**: Operación dentro de un único servicio
- **Transacción Compensatoria**: Revierte los efectos de una transacción exitosa (operación deshacer)
- **Coreografía**: Servicios reaccionan a eventos independientemente
- **Orquestación**: Coordinador central gestiona el flujo

## Dos Enfoques

### Coreografía: Orientada a Eventos

```
Servicio Órdenes    Servicio Pagos    Servicio Inventario    Servicio Envíos
        │                  │                  │                      │
        ├─ OrderCreated ───→│                  │                      │
        │  (publish)        │                  │                      │
        │                   ├─ PaymentProcessed ──→                   │
        │                   │  (publish)           │                  │
        │                   │                      ├─ ItemsReserved ──→│
        │                   │                      │  (publish)        │
        │                   │                      │                   │
        │                   │                      │← DeliveryScheduled│
        │                   │                      │  (publish)        │
```

**Descentralizada**: Sin coordinador
**Acoplamiento Laxo**: Servicios comunican vía eventos
**Trade-off**: Difícil rastrear estado general

### Orquestación: Coordinada

```
                Saga Orchestrator
                        │
         ┌──────────────┼──────────────┐
         │              │              │
    Servicio Órdenes Servicio Pagos Servicio Inventario
         │              │              │
         ├─ Crear ────→ │              │
         │← OrderId ────┤              │
         │              ├─ Procesar ──→│
         │              │← Confirmado ─┤
         │              │              ├─ Reservar ────→
         │              │              │← Reservado ───┤
```

**Centralizada**: Orquestrador controla flujo
**Visibilidad Clara**: Estado en un lugar
**Trade-off**: Orquestrador se vuelve cuello de botella

## Patrón de Coreografía

Cada servicio publica eventos, otros reaccionan. Sin coordinador central, pero estado distribuido es difícil de rastrear. Ideal para flujos simples.

## Patrón de Orquestación

Orquestador central ejecuta pasos en orden, con transacciones compensatorias en fallos. Estado claro, pero orquestrador es punto crítico.

## Coreografía vs Orquestación

| Aspecto | Coreografía | Orquestación |
|--------|------------|-------------|
| **Complejidad** | Distribuida en servicios | Centralizada en orquestador |
| **Acoplamiento** | Laxo (basado en eventos) | Más apretado (llamadas directas) |
| **Visibilidad** | Difícil rastrear | Estado claro |
| **Escalabilidad** | Altamente escalable | Cuello de botella potencial |
| **Recuperación** | Compensación por servicio | Coordinada por orquestador |
| **Pruebas** | Difícil (eventos async) | Más fácil (flujo sincrónico) |

## Cuándo Usar Cada Una

### Elige Coreografía Cuando

- Servicios naturalmente reaccionan a eventos
- Proceso de negocio relativamente simple
- Equipo valora autonomía y acoplamiento laxo
- Arquitectura event-driven ya existe

### Elige Orquestación Cuando

- Transacción compleja con muchas dependencias
- Necesitas visibilidad clara del estado de saga
- Manejo de errores centralizado preferido
- Flujo de proceso cambia frecuentemente

## Patrones de Implementación

### Transacciones Compensatorias

Cada operación forward debe tener un undo:

```
Crear Orden         → Fallo → Cancelar Orden
Procesar Pago       → Fallo → Reembolsar
Reservar Inventario → Fallo → Liberar
```

### Idempotencia

Las operaciones deben ser re-intentables de forma segura. Crear la misma orden dos veces retorna el mismo resultado.

### Timeouts y Dead-letter

Manejar servicios que no responden. Si una operación excede timeout, compensar o reintentar.

## Explicación

El patrón Saga resuelve transacciones distribuidas reemplazando garantías ACID con una serie de transacciones compensatorias. En lugar de atómico "todo o nada," las sagas aseguran "éxito en todos o deshacer en todos."

La coreografía es más autónoma y escalable pero más difícil de razonar—no hay lugar central mostrando el flujo de transacción completo. La orquestación es opuesta: más fácil entender y debugear, pero el coordinador se vuelve infraestructura crítica.

En la práctica, muchos sistemas usan enfoque híbrido: orquestación para caminos críticos (checkout, pago) y coreografía para tareas auxiliares (notificaciones, analytics). Esto balancea claridad con escalabilidad.
