# Backoff Exponencial en Go

El backoff exponencial es una estrategia de reintento que aumenta progresivamente el tiempo de espera entre reintentos para reducir carga del sistema. Esencial para manejar fallos transitorios en sistemas distribuidos, especialmente cuando múltiples clientes reintentan simultáneamente.

## Conceptos Clave

- **Retraso Inicial**: Tiempo de espera inicial (ej: 100ms)
- **Multiplicador**: Factor exponencial por reintento (típicamente 2x)
- **Retraso Máximo**: Límite para no esperar demasiado (ej: 10s)
- **Jitter**: Variación aleatoria (±10-20%) para prevenir reintentos sincronizados
- **Máximos Reintentos**: Límite de intentos (ej: 5 intentos)

## Por Qué Backoff Exponencial?

### El Problema: Manada Atronadora

Cuando múltiples clientes experimentan fallo simultáneamente y todos reintentan inmediatamente:
- Tormenta de reintentos inunda el sistema
- Sistema ya luchando no puede recuperarse
- Ocurre falla en cascada

### La Solución: Reintentos Escalonados

```
Cliente 1: ===espera(100ms)=== reintenta ===espera(200ms)=== reintenta ===espera(400ms)===
Cliente 2: ===espera(120ms)=== reintenta ===espera(240ms)=== reintenta ===espera(480ms)===
Cliente 3: ===espera(140ms)=== reintenta ===espera(260ms)=== reintenta ===espera(420ms)===

Resultado: Reintentos se distribuyen en lugar de estar sincronizados.
Sistema se recupera, solicitudes tienen éxito.
```

## Progresión de Retrasos

```
Intento 1: 100ms           (2^0 * 100ms)
Intento 2: 200ms           (2^1 * 100ms)
Intento 3: 400ms           (2^2 * 100ms)
Intento 4: 800ms           (2^3 * 100ms)
Intento 5: 1600ms → limitado → 10s (máx)

Con jitter (±20%): Cada retraso actual varía aleatoriamente
alrededor del valor exponencial
```

## Estructura del Algoritmo

```
for intento := 0; intento < maxReintentos; intento++ {
    intentar operación:
        si éxito: retornar
        
    calcular retraso:
        retraso_exponencial = retraso_base * (multiplicador ^ intento)
        retraso = mín(retraso_exponencial, retraso_máx)
        retraso += jitter_aleatorio()
        
    esperar(retraso)
}
```

## Jitter: Por Qué Importa

Sin jitter:
```
Múltiples clientes calculan mismo retraso → reintento sincronizado → manada atronadora
```

Con jitter:
```
Múltiples clientes + aleatoriedad → reintentos escalonados → sistema se estabiliza
```

Jitter típico: ±10-20% del retraso calculado

## Parámetros del Mundo Real

| Escenario | Base | Multiplicador | Máx | Reintentos | Jitter |
|-----------|------|---------------|-----|------------|--------|
| **Cliente API** | 100ms | 2x | 10s | 5 | ±10% |
| **Base de Datos** | 50ms | 2x | 5s | 7 | ±15% |
| **Llamada Servicio** | 200ms | 2x | 30s | 4 | ±20% |
| **Trabajo Batch** | 1s | 2x | 60s | 6 | ±5% |

## Explicación

El backoff exponencial resuelve el problema de reintentos en sistemas distribuidos balanceando dos preocupaciones:

1. **Tiempo de Recuperación**: Reintentos tempranos (retrasos pequeños) recuperan rápidamente de interrupciones breves
2. **Carga del Sistema**: Reintentos tardíos (retrasos grandes) previenen sobrecargar un sistema en problemas

La curva exponencial permite recuperación rápida de fallos transitorios mientras protege contra fallos en cascada. El jitter, el detalle aparentemente menor, es crucial—decorrela intentos de reintento entre clientes, previniendo tormentas de reintento sincronizadas que pueden destruir un sistema durante recuperación.

Este patrón es tan fundamental que los grandes proveedores de nube (AWS, Google Cloud, Azure) lo recomiendan en su documentación. Es la solución canónica para sistemas distribuidos resilientes.
