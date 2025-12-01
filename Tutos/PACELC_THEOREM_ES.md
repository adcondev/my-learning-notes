# Teorema PACELC en Sistemas Distribuidos

El teorema PACELC extiende CAP al abordar una limitación crítica: ¿qué sucede durante operación normal cuando las redes no están particionadas? PACELC proporciona un marco de diseño completo para condiciones de fallo y normales.

## Prerrequisitos

- Entendimiento del **Teorema CAP** (Consistencia, Disponibilidad, Tolerancia a Particiones).
- Conocimiento básico de replicación de bases de datos (síncrona vs. asíncrona).

## Conceptos Clave

- **P (Partición)**: Fallo de red entre nodos.
- **A (Disponibilidad)**: El sistema responde a las solicitudes.
- **C (Consistencia)**: Todos los nodos ven los mismos datos.
- **E (Else/Si no)**: Operación normal (sin partición).
- **L (Latencia)**: Tiempo de respuesta.

## Explicación Visual

**"Si Partición (P), elige A o C. Si no (E), elige L o C."**

```mermaid
graph TD
    Start{Estado de Red}
    
    Start -->|Partición (P)| P_Branch[Modo Fallo]
    Start -->|Normal (E)| E_Branch[Modo Normal]
    
    P_Branch -->|Elige| PA[Disponibilidad (A)]
    P_Branch -->|Elige| PC[Consistencia (C)]
    
    E_Branch -->|Elige| EL[Latencia (L)]
    E_Branch -->|Elige| EC[Consistencia (C)]
    
    PA --> Ex1[DynamoDB, Cassandra]
    PC --> Ex2[HBase, BigTable]
    EL --> Ex3[DynamoDB, Cassandra]
    EC --> Ex4[BigTable, HBase, RDBMS]
```

## Tabla Comparativa

| Tipo de Sistema | Durante Partición | Operación Normal | Ejemplos |
| :--- | :--- | :--- | :--- |
| **PA/EL** | Prefiere Disponibilidad | Prefiere Latencia | Cassandra, DynamoDB |
| **PA/EC** | Prefiere Disponibilidad | Prefiere Consistencia | MongoDB (default) |
| **PC/EL** | Prefiere Consistencia | Prefiere Latencia | BigTable, HBase |
| **PC/EC** | Prefiere Consistencia | Prefiere Consistencia | RDBMS Tradicionales (Postgres, MySQL) |

## Escenarios del Mundo Real

### 1. Feed de Redes Sociales (PA/EL)
- **Meta**: El usuario siempre debe ver *algo*, aunque sea un poco antiguo. La carga rápida es crítica.
- **Elección**: **PA** (Mostrar posts viejos si falla la red) / **EL** (Replicación async para velocidad).

### 2. Libro Mayor Bancario (PC/EC)
- **Meta**: El saldo de la cuenta debe ser 100% preciso.
- **Elección**: **PC** (Rechazar transacción si falla la red) / **EC** (Replicación sync para seguridad de datos).

## Trade-offs

- **Latencia vs. Consistencia**: En operación normal, no puedes tener ambas (latencia cero y consistencia perfecta). La replicación síncrona (Consistencia) añade latencia. La asíncrona (Latencia) arriesga pérdida de datos o datos obsoletos.
- **Disponibilidad vs. Consistencia**: Durante particiones, debes elegir entre detenerte (Consistencia) o servir datos potencialmente incorrectos (Disponibilidad).

## Siguientes Pasos

- Estudiar **Consistencia de Quórum** (R + W > N) para ajustar estos trade-offs dinámicamente.
- Aprender sobre estrategias de **Resolución de Conflictos** (Last-Write-Wins, Vector Clocks) para sistemas PA/EL.

## Etiquetas

#distributed-systems #cap-theorem #database-design #system-architecture #theory
