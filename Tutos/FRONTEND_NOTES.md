# Frontend Fundamentals

Frontend development centers on three core technologies: HTML for structure, CSS for styling, and JavaScript for interactivity. As a backend developer, think of HTML as your data structure, CSS as configuration, and JS as your application logic.

## Key Concepts

- **HTML (Structure)**: Markup language defining content hierarchy (like JSON/XML for browsers).
- **CSS (Styling)**: Declarative rules for visual presentation (selectors target elements).
- **JavaScript (Behavior)**: Programming language for DOM manipulation and event handling.
- **DOM (Document Object Model)**: Browser's in-memory tree representation of HTML.
- **Event Loop**: JS runtime model (single-threaded, async via callbacks/promises).

## HTML - Document Structure

HTML defines semantic structure. Think of it as your API contract for the browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Semantic elements improve accessibility and SEO -->
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        <section>
            <h1>Heading</h1>
            <p>Content paragraph</p>
            
            <!-- Forms capture user input -->
            <form id="userForm">
                <input type="text" name="username" placeholder="Username" required>
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025</p>
    </footer>
    
    <!-- JS loaded at end for performance -->
    <script src="script.js"></script>
</body>
</html>
```

## CSS - Styling and Layout

CSS uses selectors (like query patterns) to target elements. Modern CSS uses Flexbox/Grid for layouts.

```css
/* Box model: content → padding → border → margin */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box; /* Include padding/border in width */
}

/* Selector specificity: ID > class > element */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Flexbox for 1D layouts (row or column) */
nav {
    display: flex;
    justify-content: space-between;
    padding: 1rem;
    background: #333;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
}

nav a:hover {
    background: #555;
}

/* Grid for 2D layouts */
main {
    display: grid;
    grid-template-columns: 1fr 3fr; /* Sidebar + content */
    gap: 2rem;
    padding: 2rem;
}

/* Responsive design with media queries */
@media (max-width: 768px) {
    main {
        grid-template-columns: 1fr; /* Stack on mobile */
    }
}

/* CSS Variables for theming */
:root {
    --primary-color: #007bff;
    --spacing: 1rem;
}

button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: var(--spacing);
    cursor: pointer;
}
```

## JavaScript - DOM Manipulation and Events

JS interacts with the DOM (similar to working with a tree data structure). Events are callbacks triggered by user actions.

```javascript
// DOM selection (like querying a database)
const form = document.getElementById('userForm');
const input = document.querySelector('input[name="username"]');

// Event listener (async event handling)
form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Stop default form submission
    
    const username = input.value;
    
    // Fetch API (similar to making HTTP requests in backend)
    try {
        const response = await fetch('/api/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username })
        });
        
        const data = await response.json();
        console.log('User created:', data);
        
        // DOM manipulation
        displayUser(data);
    } catch (error) {
        console.error('Error:', error);
    }
});

// Create elements dynamically
function displayUser(user) {
    const userDiv = document.createElement('div');
    userDiv.className = 'user-card';
    userDiv.innerHTML = `
        <h3>${user.username}</h3>
        <p>ID: ${user.id}</p>
    `;
    document.querySelector('main').appendChild(userDiv);
}

// Modern JS: destructuring, arrow functions, template literals
const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' }
];

// Array methods (functional programming)
const userNames = users
    .filter(u => u.id > 0)
    .map(({ name }) => name)
    .join(', ');

console.log(userNames); // "Alice, Bob"
```

## Comparison to Backend Concepts

| Frontend Concept | Backend Equivalent |
|-----------------|-------------------|
| **DOM** | In-memory data structure/tree |
| **Event Listeners** | HTTP handlers/middleware |
| **Fetch API** | HTTP client (requests) |
| **localStorage** | Simple key-value store |
| **CSS Selectors** | Query patterns/filters |
| **Promises/Async** | Goroutines/async patterns |

## Essential Workflow

1. **Structure**: Write semantic HTML (data model).
2. **Style**: Apply CSS for layout and appearance (presentation layer).
3. **Behavior**: Add JS for interactivity and API calls (business logic).
4. **Debug**: Use browser DevTools (Console, Network, Elements tabs).

## Best Practices

- **Separation of Concerns**: Keep HTML (structure), CSS (style), JS (behavior) separate.
- **Progressive Enhancement**: Start with HTML, enhance with CSS/JS.
- **Accessibility**: Use semantic HTML, ARIA labels, keyboard navigation.
- **Performance**: Minimize DOM manipulation, debounce events, lazy load resources.
- **Mobile-First**: Design for mobile, scale up with media queries.

## Explanation

The browser parses HTML into a DOM tree, applies CSS rules via specificity matching, and executes JS in a single-threaded event loop. User interactions trigger events (callbacks), which JS handlers process asynchronously. Modern frontend mirrors backend patterns: components are like microservices, state management resembles databases, and async operations mirror concurrent request handling. The key difference is the runtime: browsers enforce security (same-origin policy), manage rendering cycles, and handle UI responsiveness.
