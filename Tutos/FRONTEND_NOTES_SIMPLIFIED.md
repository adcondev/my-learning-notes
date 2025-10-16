# Frontend Fundamentals

Frontend development centers on three technologies: HTML for structure, CSS for styling, JavaScript for interactivity. Understanding these three layers is essential for backend developers building full-stack applications.

## Key Concepts

- **HTML**: Semantic markup defining document structure and content
- **CSS**: Declarative styling and layout rules
- **JavaScript**: Event handling and DOM manipulation
- **DOM (Document Object Model)**: Browser's in-memory tree representation of HTML
- **Event Loop**: JS runtime model (single-threaded, async via callbacks)

## HTML: Document Structure

Semantic HTML provides meaning to the browser and assistive technologies.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>Header content</header>
    <main>Main content</main>
    <footer>Footer content</footer>
    <script src="app.js"></script>
</body>
</html>
```

**Key Tags**: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<form>`, `<input>`

**Semantic Benefit**: Improves accessibility, SEO, and code clarity

## CSS: Styling and Layout

CSS selectors target elements, properties define appearance, and modern layout uses Flexbox/Grid.

```css
/* Selector specificity: ID > class > element */
body { font-family: Arial; line-height: 1.6; }

/* Flexbox for 1D layouts */
nav { display: flex; justify-content: space-between; }

/* Grid for 2D layouts */
main { display: grid; grid-template-columns: 1fr 3fr; gap: 2rem; }

/* Media queries for responsiveness */
@media (max-width: 768px) {
    main { grid-template-columns: 1fr; }
}

/* CSS Variables */
:root { --primary-color: #007bff; }
button { background: var(--primary-color); }
```

**Key Concepts**:
- **Box Model**: Content → Padding → Border → Margin
- **Selectors**: Elements, classes, IDs, pseudo-classes
- **Flexbox**: 1D layout (row or column)
- **Grid**: 2D layout (rows and columns)
- **Media Queries**: Responsive design rules

## JavaScript: Interactivity

JS manipulates the DOM and responds to events in a single-threaded event loop.

```javascript
// DOM Selection (like database queries)
const button = document.querySelector('button');
const input = document.getElementById('username');

// Event Listener (async callback)
button.addEventListener('click', async (event) => {
    event.preventDefault();
    
    // Fetch API (HTTP request from browser)
    const response = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: input.value })
    });
    
    const data = await response.json();
    // Update DOM
    displayUser(data);
});

// DOM Manipulation
function displayUser(user) {
    const div = document.createElement('div');
    div.innerHTML = `<h3>${user.name}</h3>`;
    document.querySelector('main').appendChild(div);
}
```

**Key Patterns**:
- **DOM Queries**: `querySelector`, `getElementById`, etc.
- **Event Listeners**: `addEventListener`, event handlers
- **Fetch API**: HTTP requests from browser
- **Promises/Async-Await**: Asynchronous operations
- **Array Methods**: `map`, `filter`, `reduce` for data transformation

## Frontend Architecture

```
┌─────────────────────────────────────┐
│         User Interaction            │ (Click, Type, Scroll)
├─────────────────────────────────────┤
│    JavaScript (Event Handlers)      │ (React, Vue, Vanilla)
├─────────────────────────────────────┤
│           DOM                       │ (In-Memory Tree)
├─────────────────────────────────────┤
│         Browser Engine              │ (Parsing, Rendering)
├─────────────────────────────────────┤
│     HTTP → Backend API              │ (Fetch, WebSocket)
└─────────────────────────────────────┘
```

## Frontend vs Backend Concepts

| Frontend | Backend Equivalent |
|----------|-------------------|
| DOM | Data structures |
| Event Listeners | HTTP handlers/middleware |
| Fetch API | HTTP client |
| localStorage | Key-value cache |
| CSS Selectors | Query patterns |
| Promises/Async | Goroutines/async patterns |

## Performance Considerations

- **Minimize DOM Manipulation**: Expensive operation, batch updates
- **Debounce Events**: Prevent excessive callbacks (e.g., on scroll/resize)
- **Lazy Load Resources**: Load images/scripts only when needed
- **Code Splitting**: Load code by route, not all at once

## Common Patterns

### Form Handling

```javascript
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    // Send to server
});
```

### Dynamic Content

```javascript
// Clear and repopulate
const container = document.getElementById('items');
container.innerHTML = ''; // Clear
items.forEach(item => {
    container.innerHTML += `<div>${item.name}</div>`;
});
```

### API Integration

```javascript
// Fetch and update UI
async function loadUsers() {
    try {
        const response = await fetch('/api/users');
        const users = await response.json();
        renderUsers(users);
    } catch (error) {
        displayError(error);
    }
}
```

## Explanation

Frontend is ultimately about two things: presenting data (HTML/CSS) and responding to user actions (JavaScript). The browser is the runtime, the DOM is your data structure, events are your interrupt handlers.

Backend developers often underestimate frontend because it seems simpler. In reality, frontend complexity comes from interactivity: managing state, handling events, async operations, and keeping the UI synchronized with data. Modern frameworks (React, Vue) manage this complexity through component abstractions.

The key difference from backend: frontend is **declarative** (CSS says "be red", not "color this pixel"). Backend is **imperative** (code says "do this step by step"). Understanding this paradigm shift is crucial.