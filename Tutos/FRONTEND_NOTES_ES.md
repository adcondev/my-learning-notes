# Fundamentos de Frontend

El desarrollo de frontend se centra en tres tecnologías: HTML para estructura, CSS para estilizado, JavaScript para interactividad. Entender estas tres capas es esencial para desarrolladores backend construyendo aplicaciones full-stack.

## Conceptos Clave

- **HTML**: Marcado semántico que define estructura y contenido del documento
- **CSS**: Reglas declarativas de estilizado y layout
- **JavaScript**: Manejo de eventos y manipulación del DOM
- **DOM (Document Object Model)**: Representación del árbol en-memoria del navegador del HTML
- **Event Loop**: Modelo de runtime de JS (single-threaded, async vía callbacks)

## HTML: Estructura del Documento

HTML semántico proporciona significado al navegador y tecnologías asistivas.

**Etiquetas Clave**: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<form>`, `<input>`

**Beneficio Semántico**: Mejora accesibilidad, SEO, y claridad del código

## CSS: Estilizado y Layout

Los selectores CSS apuntan elementos, las propiedades definen apariencia, y layouts modernos usan Flexbox/Grid.

**Conceptos Clave**:

- **Box Model**: Contenido → Padding → Borde → Margin
- **Selectores**: Elementos, clases, IDs, pseudo-clases
- **Flexbox**: Layout 1D (fila o columna)
- **Grid**: Layout 2D (filas y columnas)
- **Media Queries**: Reglas de diseño responsivo

## JavaScript: Interactividad

JS manipula el DOM y responde a eventos en un event loop single-threaded.

**Patrones Clave**:

- **Consultas DOM**: `querySelector`, `getElementById`, etc.
- **Event Listeners**: `addEventListener`, handlers de eventos
- **Fetch API**: Solicitudes HTTP desde el navegador
- **Promises/Async-Await**: Operaciones asincrónicas
- **Array Methods**: `map`, `filter`, `reduce` para transformación de datos

## Arquitectura Frontend

```
┌─────────────────────────────────────┐
│    Interacción del Usuario          │ (Click, Escribir, Scroll)
├─────────────────────────────────────┤
│   JavaScript (Manejadores)          │ (React, Vue, Vanilla)
├─────────────────────────────────────┤
│            DOM                      │ (Árbol En-Memoria)
├─────────────────────────────────────┤
│      Motor del Navegador            │ (Parsing, Rendering)
├─────────────────────────────────────┤
│     HTTP → API Backend              │ (Fetch, WebSocket)
└─────────────────────────────────────┘
```

## Frontend vs Backend: Conceptos

| Frontend | Equivalente Backend |
|----------|-------------------|
| DOM | Estructuras de datos |
| Event Listeners | Handlers HTTP/middleware |
| Fetch API | Cliente HTTP |
| localStorage | Cache clave-valor |
| CSS Selectors | Patrones de consulta |
| Promises/Async | Goroutines/patrones async |

## Consideraciones de Rendimiento

- **Minimizar Manipulación del DOM**: Operación costosa, agrupar actualizaciones
- **Debounce de Eventos**: Prevenir callbacks excesivos (ej: en scroll/resize)
- **Lazy Load de Recursos**: Cargar imágenes/scripts solo cuando se necesitan
- **Code Splitting**: Cargar código por ruta, no todo de una vez

## Patrones Comunes

### Manejo de Formularios

Obtener datos del formulario, prevenir comportamiento por defecto, enviar al servidor.

### Contenido Dinámico

Limpiar y repoblar contenedores. Crear elementos dinámicamente con datos.

### Integración de API

Fetch de datos, manejo de errores, actualizar UI.

## Explicación

Frontend es en última instancia sobre dos cosas: presentar datos (HTML/CSS) y responder a acciones del usuario (JavaScript). El navegador es el runtime, el DOM es tu estructura de datos, eventos son tus handlers de interrupción.

Los desarrolladores backend a menudo subestiman frontend porque parece más simple. En realidad, la complejidad de frontend viene de la interactividad: manejar estado, procesar eventos, operaciones async, y mantener la UI sincronizada con datos. Los frameworks modernos (React, Vue) manejan esta complejidad a través de abstracciones de componentes.

La diferencia clave respecto a backend: frontend es **declarativo** (CSS dice "sé rojo", no "colorea este pixel"). Backend es **imperativo** (código dice "haz este paso a paso"). Entender este cambio de paradigma es crucial.
