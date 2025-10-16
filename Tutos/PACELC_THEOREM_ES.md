# Teorema PACELC en Sistemas Distribuidos

El teorema PACELC extiende CAP al abordar una limitación crítica: ¿qué sucede durante operación normal cuando las redes no están particionadas? PACELC proporciona un marco de diseño completo para condiciones de fallo y normales.

## Fórmula PACELC

Si hay Partición de red (P): elige Disponibilidad (A) o Consistencia (C). Si no (E) en operación normal: elige Latencia (L) o Consistencia (C).

## Conceptos Clave

### Durante Particiones (PAC)

- **Partición (P)**: Fallos de red o pérdida de mensajes entre nodos
- **Disponibilidad (A)**: El sistema responde a cada solicitud, incluso durante fallos
- **Consistencia (C)**: Todos los nodos ven los mismos datos simultáneamente

### Durante Operación Normal (ELC)

- **Si No (E)**: Operación normal sin particiones de red
- **Latencia (L)**: Tiempos de respuesta rápidos para operaciones lectura/escritura
- **Consistencia (C)**: Garantías de consistencia fuerte durante operación normal

## Matriz de Trade-offs de PACELC

| Clasificación | Durante Partición | Operación Normal | Ejemplos |
|---------------|-------------------|-----------------|----------|
| **PA/EL** | Disponibilidad | Latencia | Cassandra, DynamoDB |
| **PA/EC** | Disponibilidad | Consistencia | MongoDB, CouchDB |
| **PC/EL** | Consistencia | Latencia | BigTable, HBase |
| **PC/EC** | Consistencia | Consistencia | RDBMS Tradicionales |

## Diagrama de Compromisos

```
Partición de Red
    │
    ├─ Opción A: Disponibilidad
    │  • Acepta datos obsoletos
    │  • Sistema sigue funcionando
    │  • Ejemplo: Cassandra
    │
    └─ Opción C: Consistencia
       • Rechaza solicitudes
       • Sistema indisponible
       • Ejemplo: HBase

Operación Normal
    │
    ├─ Opción L: Latencia
    │  • Replicación asincrónica
    │  • Respuestas rápidas
    │  • Consistencia eventual
    │
    └─ Opción C: Consistencia
       • Replicación síncrona
       • Respuestas más lentas
       • Consistencia inmediata
```

## Ejemplos del Mundo Real

### Cassandra (PA/EL)

- **Partición**: Elige disponibilidad → acepta escrituras en todos los nodos alcanzables
- **Normal**: Elige latencia → replicación asincrónica
- **Resultado**: Altamente disponible, muy rápido, eventualmente consistente
- **Caso de Uso**: Feeds de redes sociales, datos IoT

### MongoDB (PA/EC)

- **Partición**: Elige disponibilidad → lee desde secundarios
- **Normal**: Elige consistencia → espera confirmación de mayoría
- **Resultado**: Equilibrado con consistencia sintonizable
- **Caso de Uso**: Aplicaciones web

### Google Spanner (PC/EC)

- **Partición**: Elige consistencia → rechaza si quórum no disponible
- **Normal**: Elige consistencia → replicación síncrona con TrueTime
- **Resultado**: Consistencia fuerte en todo momento
- **Caso de Uso**: Sistemas financieros globales

## Marco de Decisión PACELC

### Durante Partición de Red

¿Tu aplicación tolera datos obsoletos?
- **Sí** → Elige Disponibilidad (PA)
- **No** → Elige Consistencia (PC)

### Durante Operación Normal

¿Qué importa más para la experiencia del usuario?
- **Respuestas rápidas** → Elige Latencia (EL)
- **Siempre datos precisos** → Elige Consistencia (EC)

### Contexto de Negocio

¿Cuáles son las consecuencias de inconsistencia?
- **Leve** → PA/EL (social media, analytics)
- **Severa** → PC/EC (finanzas, crítico)
- **Mixto** → PA/EC o PC/EL (e-commerce)

## Patrones de Implementación

### PA/EL: Disponibilidad y Latencia

Patrón: Replicación eventual asincrónica
Comportamiento: Acepta todas las operaciones, resuelve conflictos después
Trade-off: Rendimiento máximo, consistencia débil
Ejemplo: Usuario publica en red social, ve confirmación inmediatamente, otros ven después

### PA/EC: Disponibilidad con Consistencia Normal

Patrón: Niveles de consistencia sintonizable
Comportamiento: Disponible en particiones, consistente cuando es posible
Trade-off: Equilibrio, con garantías configurables
Ejemplo: Aplicación web que tolera desconexiones temporales

### PC/EL: Consistencia de Partición, Latencia Normal

Patrón: Protocolos de consenso optimizados
Comportamiento: Rechaza en particiones, optimizado para velocidad cuando saludable
Trade-off: Datos precisos, disponibilidad limitada
Ejemplo: Sistema de analytics que necesita datos exactos

### PC/EC: Consistencia Siempre

Patrón: Replicación síncrona y consenso
Comportamiento: Consistencia garantizada en todo momento
Trade-off: Máxima confiabilidad, latencia y complejidad
Ejemplo: Sistemas bancarios, aplicaciones críticas

## PACELC vs CAP: Diferencias Clave

| Aspecto | CAP | PACELC |
|--------|-----|--------|
| **Alcance** | Solo particiones | Particiones + operación normal |
| **Enfoque** | Disponibilidad vs Consistencia | Agrega Latencia vs Consistencia |
| **Completitud** | Vista parcial | Marco completo |
| **Orientación de Diseño** | Escenarios de fallo | Ciclo de vida completo |

## Consideraciones de Diseño del Sistema

- **Criticidad de Datos**: ¿Qué tan importante es que todos los nodos tengan datos idénticos?
- **Expectativas del Usuario**: ¿Esperan respuestas instantáneas o datos precisos?
- **Distribución Geográfica**: ¿Usuarios y servidores distribuidos globalmente?
- **Recuperación de Fallos**: ¿Qué tan rápido detecta y se recupera tu sistema?
- **Complejidad Operacional**: ¿Tu equipo puede manejar consistencia eventual?

## Conclusión

PACELC proporciona un marco más completo que CAP para entender trade-offs de sistemas distribuidos. Al considerar ambos escenarios de partición y operación normal, ayuda a arquitectos tomar decisiones informadas sobre:

- **Estrategias de Replicación**: Síncrona vs asincrónica
- **Modelos de Consistencia**: Fuerte, eventual, o sintonizable
- **Características de Rendimiento**: Optimizar para latencia o consistencia
- **Manejo de Fallos**: Comportamiento en particiones

Recuerda: No hay opción "mejor"—solo el trade-off más apropiado para tu caso de uso específico y requisitos de negocio.
