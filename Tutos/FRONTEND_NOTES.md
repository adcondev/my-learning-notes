# Frontend Fundamentals

A minimal guide to HTML, CSS, and JavaScript for backend developers. Focuses on core concepts needed to build interactive web interfaces.

## Key Concepts

- **HTML**: Structure and content of the page (nouns - what things are)
- **CSS**: Visual styling and layout (adjectives - how things look)
- **JavaScript**: Behavior and interactivity (verbs - what things do)
- **DOM**: Document Object Model - the tree structure representing HTML elements that JavaScript manipulates

## HTML - Structure

HTML defines the semantic structure using tags. Think of it like defining data structures.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Semantic elements -->
    <header>
        <h1>Welcome</h1>
        <nav>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        <section>
            <h2>Content Title</h2>
            <p>Text content here</p>
            
            <!-- Form inputs -->
            <form id="userForm">
                <input type="text" id="username" placeholder="Username">
                <button type="submit">Submit</button>
            </form>
        </section>
    </main>
    
    <script src="script.js"></script>
</body>
</html>
```

### Common HTML Elements

| Element | Purpose | Example |
|---------|---------|---------|
| `<div>` | Generic container | `<div class="container">...</div>` |
| `<span>` | Inline container | `<span class="highlight">text</span>` |
| `<input>` | User input | `<input type="text" id="name">` |
| `<button>` | Clickable button | `<button onclick="handleClick()">Click</button>` |
| `<ul>/<li>` | Lists | `<ul><li>Item</li></ul>` |

## CSS - Styling

CSS selects elements and applies styles. Similar to configuration files defining appearance.

```css
/* Select by tag */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

/* Select by class (reusable) */
.container {
    max-width: 800px;
    margin: 0 auto;
}

/* Select by ID (unique) */
#username {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Hover state */
button:hover {
    background-color: #0056b3;
    cursor: pointer;
}

/* Flexbox for layout */
.flex-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

### CSS Selectors Priority

```
ID (#username) > Class (.container) > Tag (div)
```

### Box Model (Every Element)

```
┌─────────────────────────────────┐
│         Margin (outside)        │
│  ┌──────────────────────────┐   │
│  │    Border                │   │
│  │  ┌────────────────────┐  │   │
│  │  │  Padding           │  │   │
│  │  │  ┌──────────────┐  │  │   │
│  │  │  │   Content    │  │  │   │
│  │  │  └──────────────┘  │  │   │
│  │  └────────────────────┘  │   │
│  └──────────────────────────┘   │
└─────────────────────────────────┘
```

## JavaScript - Behavior

JavaScript manipulates the DOM and handles events. Think of it as your application logic running in the browser.

```javascript
// DOM Manipulation
const element = document.getElementById('username');
const elements = document.querySelectorAll('.container');

element.textContent = 'New text';
element.style.color = 'blue';
element.classList.add('active');

// Event Listeners
document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Stop form submission
    
    const username = document.getElementById('username').value;
    console.log('Username:', username);
});

// Fetch API (like HTTP requests in Go/Python)
fetch('https://api.example.com/users')
    .then(response => response.json())
    .then(data => {
        console.log('Users:', data);
        displayUsers(data);
    })
    .catch(error => console.error('Error:', error));

// Async/Await (cleaner syntax)
async function getUsers() {
    try {
        const response = await fetch('https://api.example.com/users');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Arrow functions (like lambdas)
const add = (a, b) => a + b;
const double = x => x * 2;
```

### JavaScript Essentials for Backend Devs

| Concept | Similar To | Example |
|---------|-----------|---------|
| `let`/`const` | Variables | `const name = "John";` |
| Arrow functions | Lambdas | `const fn = (x) => x * 2;` |
| Promises | Futures/Async | `fetch(url).then(...)` |
| `async/await` | async/await in Python | `await fetch(url)` |
| Event listeners | Callbacks | `btn.addEventListener('click', fn)` |

## Complete Minimal Example

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial; padding: 20px; }
        .user-card { 
            border: 1px solid #ddd; 
            padding: 10px; 
            margin: 10px 0; 
        }
        button { 
            padding: 8px 16px; 
            background: #007bff; 
            color: white; 
            border: none; 
            cursor: pointer; 
        }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <h1>User List</h1>
    <button id="loadUsers">Load Users</button>
    <div id="userContainer"></div>

    <script>
        document.getElementById('loadUsers').addEventListener('click', async () => {
            try {
                const response = await fetch('https://jsonplaceholder.typicode.com/users?_limit=3');
                const users = await response.json();
                
                const container = document.getElementById('userContainer');
                container.innerHTML = users.map(user => `
                    <div class="user-card">
                        <h3>${user.name}</h3>
                        <p>Email: ${user.email}</p>
                    </div>
                `).join('');
            } catch (error) {
                console.error('Failed to load users:', error);
            }
        });
    </script>
</body>
</html>
```

## Explanation

### HTML
- **Structure**: Defines what elements exist (headings, paragraphs, forms)
- **Semantic tags**: Use meaningful tags (`<header>`, `<main>`, `<nav>`) instead of just `<div>`
- **Attributes**: Add metadata (`id`, `class`, `href`, `type`)

### CSS
- **Selectors**: Target elements to style (`.class`, `#id`, `tag`)
- **Box Model**: Every element has content, padding, border, margin
- **Flexbox**: Modern layout system (`display: flex`) for responsive designs
- **Use classes** for reusable styles, IDs for unique elements

### JavaScript
- **DOM API**: Methods to find and modify HTML elements
- **Events**: Respond to user actions (clicks, form submissions)
- **Fetch API**: Make HTTP requests (similar to `requests` in Python or `http.Get` in Go)
- **Async/Await**: Handle asynchronous operations cleanly

### Backend Developer Tips
1. **HTML is your data structure** - defines what exists
2. **CSS is your configuration** - defines how it looks
3. **JavaScript is your logic** - defines behavior and handles API calls
4. **Browser DevTools** (F12) is your debugger - inspect elements, see console logs, debug JavaScript

This covers the essential 20% you'll use 80% of the time. Modern frameworks (React, Vue) build on these fundamentals but follow the same core principles.
