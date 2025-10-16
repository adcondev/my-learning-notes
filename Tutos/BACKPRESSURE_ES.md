# Contrapresión en Go

La contrapresión previene que un productor rápido abrume a un consumidor lento controlando el flujo de datos. En Go, usa canales bufferizados y `select` para señalizar o bloquear cuando los búferes se llenan, forzando al productor a esperar.

## Conceptos Clave

- **Productor**: Envía datos a un canal
- **Consumidor**: Lee del canal
- **Contrapresión**: Ocurre cuando el búfer del canal se llena; el envío se bloquea, ralentizando la producción
- **Canales Bufferizados**: Canales con capacidad que almacenan valores antes de bloquear
- **Select con Default**: Operaciones no-bloqueantes en canales para manejar contrapresión

## Cómo Funciona

```
Productor Rápido → [Búfer: capacidad=3] → Consumidor Lento
                          ↑
                  Cuando está lleno: Productor se bloquea
                  Fuerza al productor a esperar
                  Sistema alcanza equilibrio
```

Cuando un productor intenta enviar en un canal lleno:
- La operación de envío se bloquea
- El productor deja de generar datos
- Este throttling natural previene desbordamiento de memoria
- El sistema alcanza equilibrio basado en velocidad del consumidor

## Patrón: Select con Caso Default

```
select {
    case ch <- value:      // Envío no-bloqueante
        // Éxito
    default:               // Se ejecuta si envío se bloquearía
        // Manejar contrapresión: reintentar, esperar, descartar, agregar
}
```

## Patrón: Dimensionamiento del Búfer

- **Tamaño búfer = 0** (sin buffer): Productor se bloquea hasta que receptor esté listo
- **Tamaño búfer = 1-10**: Búfer pequeño, señal rápida de contrapresión
- **Tamaño búfer = grande**: Buffering alto, señal lenta de contrapresión

Elegir tamaño de búfer determina cuánto "lag" tolera el sistema antes de aplicar contrapresión.

## Propagación de Contrapresión

```
Servicio A → Canal (tamaño=5) → Servicio B
   ↓                               ↓
[Rápido]                    [Lento - 2 msgs/seg]

Línea de Tiempo:
- Segundos 1-2: Búfer se llena (5 mensajes encolados)
- Segundo 3: Servicio A se bloquea en envío (contrapresión aplica)
- Servicio A deja de producir hasta que B consume algunos
- Sistema auto-throttle a velocidad de B
```

## Escenario del Mundo Real

Sin contrapresión: Eventos de alta frecuencia inundan un procesador lento, causando agotamiento de memoria y crash.

Con contrapresión: Productor de eventos automáticamente se ralentiza cuando procesador no puede mantenerse al día. Sistema permanece estable incluso bajo presión.

## Explicación

La contrapresión es la solución elegante de Go al desajuste productor-consumidor. Al usar canales bufferizados con capacidad limitada, los consumidores lentos naturalmente reducen la velocidad de productores rápidos sin gestión de congestión explícita. El búfer del canal actúa como amortiguador—cuando está lleno, el productor se bloquea, previniendo desbordamiento de memoria.

Esto es especialmente poderoso en microservicios: cuando servicio aguas abajo está sobrecargado, el servicio aguas arriba automáticamente se detiene en lugar de encolar infinitos mensajes. El resultado es degradación elegante en lugar de falla en cascada.

La idea clave: canales bufferizados crean control de flujo implícito. Sin necesidad de algoritmos complejos de congestión—la primitiva del lenguaje lo maneja naturalmente.
