# Descubrimiento de Servicios en Microservicios

El descubrimiento de servicios gestiona y expone ubicaciones de servicios, permitiendo que los microservicios se localicen y comuniquen dinámicamente. Desvincula la ubicación del servicio de direcciones codificadas, habilitando auto-escalado y resiliencia.

## Conceptos Clave

- **Registro de Servicios**: Catálogo centralizado de instancias de servicios disponibles y sus direcciones
- **Registro**: El servicio se registra al iniciar, se desregistra al apagar
- **Chequeos de Salud**: Sondeos periódicos para detectar y remover instancias no saludables
- **Descubrimiento del Lado del Cliente**: Los clientes consultan el registro para encontrar servicios
- **Descubrimiento del Lado del Servidor**: El balanceador de carga consulta el registro internamente

## Dos Enfoques

### Descubrimiento del Lado del Cliente

```
Cliente             Registro            Servicio A
  │                   │                    │
  ├─ Consultar "api"─→│                    │
  │                   │← Retorna instancias│
  │                   │  [A1: host:8080,   │
  │                   │   A2: host:8081]   │
  │                                        │
  ├─ Elegir A1 ──────────→ Solicitud
  │                        Respuesta ←────┤
```

**Ventajas**: Conexión directa, control total
**Desventajas**: Clientes manejan balanceo de carga y failover

### Descubrimiento del Lado del Servidor

```
Cliente        Balanceador        Registro        Servicio A
  │              │                  │               │
  ├─ Solicitud──→│                  │               │
  │              ├─ Consultar ────→ │               │
  │              │← Lista           │               │
  │              │                  │               │
  │              ├─────────────────────→ Reenviar
  │              │← Respuesta ──────────┤
  │← Respuesta ──┤                      │
```

**Ventajas**: Clientes simplificados, balanceador maneja complejidad
**Desventajas**: Balanceador se vuelve cuello de botella potencial

## Patrones de Registro de Servicios

| Patrón | Herramienta | Caso de Uso |
|--------|-----------|------------|
| **Consul** | Registro explícito | Microservicios en VMs, K8s auto-administrado |
| **Kubernetes DNS** | Automático (built-in) | Cualquier servicio contenedorizado |
| **Eureka** | Registro, heartbeat | Spring Boot, stack Netflix |
| **Proveedor Cloud** | AWS/GCP/Azure | Aplicaciones cloud-native |

## Patrón de Registro

```
Servicio inicia
  │
  ├─ Registrarse en el registro
  │  [nombre: "user-service",
  │   dirección: "10.0.1.5",
  │   puerto: 8080,
  │   chequeoSalud: "GET /health"]
  │
  ├─ Latido periódico (ej: cada 5s)
  │  "Aún estoy vivo"
  │
  ├─ En caso de fallo o apagado
  │  Desregistrarse
  │
  └─ Registro elimina entradas obsoletas
     después del timeout del latido
```

## Chequeos de Salud

```
Registro        Servicio
  │               │
  ├─ GET /health ─→│
  │                │
  │← 200 OK ──────┤ (Saludable: mantener registrado)
  
  ├─ GET /health ─→│
  │                │
  │  (Sin respuesta)│ (Timeout: marcar no saludable)
  │
  └─ Después de N fallos: Remover del registro
```

## Consideraciones de Implementación

### Qué Registrar

- Nombre del servicio (identificador único)
- Dirección de red y puerto
- Versión/tags para filtrado
- Endpoint de chequeo de salud
- Metadata (región, flag canary, etc.)

### Estrategias de Chequeo de Salud

- **Pasiva**: Clientes reportan fallos
- **Activa**: Registro pinguea servicio
- **Externa**: Monitor separado verifica
- **Aplicación**: Servicio auto-reporta

## Matriz Comparativa

| Aspecto | Lado del Cliente | Lado del Servidor |
|--------|-----------------|------------------|
| **Complejidad** | Alta (clientes) | Baja (clientes) |
| **Balanceo de Carga** | Librería cliente | Balanceador |
| **Latencia** | Menor (directa) | Ligeramente mayor |
| **Escalabilidad** | Lineal con clientes | Cuello en balanceador |
| **Manejo de Fallos** | Por cliente | Centralizado |
| **Ejemplo** | Consul + librería | Kubernetes |

## Explicación

El descubrimiento de servicios resuelve un problema fundamental en microservicios: ¿cómo se encuentran los servicios entre sí cuando cambian ubicaciones? Codificar direcciones rompe el auto-escalado y resiliencia; el descubrimiento de servicios hace que la ubicación sea una preocupación de runtime.

La elección entre cliente-lado y servidor-lado depende de tu infraestructura:
- **Cliente-lado** te da control granular y conexiones directas, ideal si administras tu propia infraestructura
- **Servidor-lado** simplifica clientes y centraliza complejidad, ideal en ambientes cloud-native (Kubernetes, serverless)

Los chequeos de salud previenen solicitudes a servicios muertos. Sin ellos, los clientes reintentan instancias fallidas repetidamente. El ciclo de vida de registro/desregistro asegura que el registro se mantenga preciso.

Las plataformas modernas (Kubernetes, service meshes) automatizan mucho de esto. Entender los patrones subyacentes ayuda cuando se construyen soluciones personalizadas o se depuran problemas.
