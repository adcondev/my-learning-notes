# Patrones de Pruebas en Go

Las pruebas en Go siguen una jerarquía desde pruebas unitarias aisladas hasta integración del sistema completo. Cada patrón sirve propósitos diferentes: verificar funciones individuales, aislar dependencias, probar con comportamiento realista, o validar flujos completos.

## Conceptos Clave

- **Pruebas Unitarias**: Pruebas de funciones individuales con mocks
- **Mocks**: Simulan dependencias con respuestas predeterminadas
- **Fakes**: Implementaciones funcionales con comportamiento simplificado
- **Pruebas de Integración**: Múltiples componentes juntos
- **E2E (End-to-End)**: Flujos completos a través de interfaces reales

## Pirámide de Pruebas

```
        ╱╲
       ╱  ╲  Pruebas E2E (5%)
      ╱    ╲ Lentas, frágiles, atrapa problemas del sistema
     ╱──────╲
    ╱        ╲ Pruebas de Integración (15%)
   ╱          ╲ Velocidad moderada, comportamiento realista
  ╱────────────╲
 ╱              ╲ Pruebas Unitarias (80%)
 ╱________________╲ Rápidas, aisladas, confiables
```

80% unitarias, 15% integración, 5% E2E para balance óptimo.

## Patrón de Prueba Unitaria: Orientada a Tabla

Define casos de prueba como datos, ejecuta cada uno. Fácil agregar casos, parametrización clara.

## Patrón de Mock

Simula dependencias con comportamiento exacto. Control total, pero no prueba integración real.

## Patrón de Fake

Implementación funcional simplificada. Más realista, pero requiere implementación.

## Selección de Pruebas

| Tipo de Prueba | Velocidad | Alcance | Cuándo |
|----------------|-----------|---------|--------|
| **Unitaria** | Rápida | Función individual | Siempre (mayoría) |
| **Mock** | Rápida | Función con deps aisladas | Cuando necesitas control exacto |
| **Fake** | Media | Servicio + almacenamiento simplificado | Verificación de integración |
| **E2E** | Lenta | Sistema completo | Solo caminos críticos |

## Ejecución

```bash
# Todas las pruebas
go test ./...

# Prueba específica
go test -run TestName ./...

# Sin pruebas lentas
go test -short ./...

# Con cobertura
go test -cover ./...
```

## Mejores Prácticas

- **Probar Comportamiento, No Implementación**: Verifica qué hace la función, no cómo lo hace
- **Nombres Claros**: `TestUserService_CreateUser_ValidInput` mejor que `TestCreate`
- **Un Foco de Aserción**: Cada prueba debe verificar una cosa
- **Pruebas Paralelas**: Usa `t.Parallel()` para acelerar
- **Fallar Rápido**: Retornar temprano en fallos de setup

## Patrones Comunes

### Setup y Teardown

```
func setupTest() *Service {
    // Crear dependencias
    db := setupDatabase()
    cache := setupCache()
    return NewService(db, cache)
}

func TestSomething(t *testing.T) {
    service := setupTest()
    defer cleanupTest()
    
    // Test...
}
```

### Subtests

```
func TestService(t *testing.T) {
    t.Run("create user", func(t *testing.T) {
        // Código de prueba
    })
    t.Run("delete user", func(t *testing.T) {
        // Código de prueba
    })
}
```

## Explicación

La filosofía de pruebas de Go es pragmática: funciones simples, ceremonia mínima. El paquete estándar testing carece de librería de aserciones, forzando explicititud sobre qué estás verificando. Esto es intencional—mensajes de error claros importan más que DSLs.

La pirámide existe por costo: pruebas unitarias son baratas (milisegundos), E2E caras (segundos). Escribe muchas pruebas rápidas para atrapar regresiones rápidamente, menos pruebas lentas para caminos críticos. Esto proporciona feedback rápido durante desarrollo mientras asegura que funcionalidad core funciona end-to-end.

Las pruebas orientadas a tabla aprovechan la simplicidad de Go para escalar: agregar casos de prueba es agregar filas, sin funciones nuevas necesarias. Este patrón se vuelve idioma Go una vez que escribes algunos.
