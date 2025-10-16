# SOLID Principles in Go

SOLID represents five design principles that enable maintainable, scalable, and testable code. Go's implicit interfaces and composition naturally align with these principles, making SOLID a practical guide rather than strict rules.

## Key Concepts

- **Single Responsibility (SRP)**: Each type has one reason to change
- **Open/Closed (OCP)**: Open for extension, closed for modification
- **Liskov Substitution (LSP)**: Implementations are interchangeable without breaking contracts
- **Interface Segregation (ISP)**: Clients shouldn't depend on interfaces they don't use
- **Dependency Inversion (DIP)**: Depend on abstractions, not concrete types

## 1. Single Responsibility Principle

Each struct should have exactly one reason to change. In Go, this means separating concerns into distinct types.

### The Problem

```go
type User struct {
    ID    int
    Name  string
}

// ❌ Multiple responsibilities mixed
func (u *User) ValidateEmail() error     { /*...*/ }
func (u *User) SaveToDatabase() error    { /*...*/ }
func (u *User) SendWelcomeEmail() error  { /*...*/ }
func (u *User) FormatJSON() string       { /*...*/ }
```

Changes to validation, persistence, email sending, or formatting all modify `User`. This creates tight coupling and makes testing difficult.

### The Solution

```go
// Each type has single responsibility
type User struct {
    ID    int
    Name  string
}

type UserValidator struct{}
func (v *UserValidator) ValidateEmail(u *User) error { /*...*/ }

type UserRepository struct{}
func (r *UserRepository) Save(u *User) error { /*...*/ }

type EmailService struct{}
func (e *EmailService) SendWelcome(u *User) error { /*...*/ }

type UserFormatter struct{}
func (f *UserFormatter) ToJSON(u *User) string { /*...*/ }
```

**Trade-off**: More files/types, but each is simpler and testable in isolation.

## 2. Open/Closed Principle

Software should be open for extension without modifying existing code. Use interfaces to add behavior.

### The Problem

```go
func ProcessPayment(amount float64, method string) error {
    switch method {
    case "credit_card":
        return chargeCard(amount)
    case "paypal":
        return chargePayPal(amount)
    // Adding new payment methods requires modifying this function
    case "crypto":
        return chargeCrypto(amount)
    }
}
```

Every new payment method forces code modification, risking existing functionality.

### The Solution

```go
type PaymentProcessor interface {
    Process(amount float64) error
}

type CreditCard struct{ /*...*/ }
func (c *CreditCard) Process(amount float64) error { /*...*/ }

type PayPal struct{ /*...*/ }
func (p *PayPal) Process(amount float64) error { /*...*/ }

// New payment method: no modification to existing code
type Cryptocurrency struct{ /*...*/ }
func (c *Cryptocurrency) Process(amount float64) error { /*...*/ }

func HandlePayment(processor PaymentProcessor, amount float64) error {
    return processor.Process(amount) // Works with any implementation
}
```

**Trade-off**: Requires designing for extensibility upfront, but enables safe additions later.

## 3. Liskov Substitution Principle

All implementations of an interface must be substitutable without breaking the program. The contract must be honored.

### The Problem

```go
type Bird interface {
    Fly() error
}

type Eagle struct{}
func (e *Eagle) Fly() error {
    return fmt.Errorf("flying...") // Normal behavior
}

type Penguin struct{}
func (p *Penguin) Fly() error {
    return fmt.Errorf("can't fly") // Violates contract
}

func MakeFly(bird Bird) {
    if err := bird.Fly(); err != nil {
        panic(err) // Penguin crashes the program
    }
}
```

`Penguin` implements the interface but violates the expected behavior, causing runtime errors.

### The Solution

```go
// Separate interfaces by capability
type Bird interface {
    Move() string
}

type FlyingBird interface {
    Bird
    Fly() string
}

type SwimmingBird interface {
    Bird
    Swim() string
}

type Eagle struct{}
func (e *Eagle) Move() string { return "moving" }
func (e *Eagle) Fly() string  { return "flying" }

type Penguin struct{}
func (p *Penguin) Move() string { return "moving" }
func (p *Penguin) Swim() string { return "swimming" }

// Type system prevents misuse
func MakeFly(bird FlyingBird) { bird.Fly() }     // Only for flying birds
func MakeSwim(bird SwimmingBird) { bird.Swim() } // Only for swimming birds
```

**Trade-off**: Compiler catches violations, prevents subtle runtime bugs.

## 4. Interface Segregation Principle

Clients shouldn't depend on interfaces they don't use. Prefer many small interfaces over few large ones.

### The Problem

```go
// ❌ Fat interface
type Worker interface {
    Work()
    Eat()
    Sleep()
    TakeMedicalLeave()
    GetSalary() float64
}

type Robot struct{}
func (r *Robot) Work() { /*...*/ }
func (r *Robot) Eat()  { /*...*/ }    // Irrelevant
func (r *Robot) Sleep() { /*...*/ }   // Irrelevant
func (r *Robot) TakeMedicalLeave() {} // Irrelevant
func (r *Robot) GetSalary() float64 { return 0 } // Wrong
```

`Robot` forced to implement methods that don't apply to robots.

### The Solution

```go
// ✅ Small, focused interfaces
type Workable interface {
    Work()
}

type Eatable interface {
    Eat()
}

type Payable interface {
    GetSalary() float64
}

type Human struct{}
func (h *Human) Work() { /*...*/ }
func (h *Human) Eat()  { /*...*/ }
func (h *Human) GetSalary() float64 { /*...*/ }

type Robot struct{}
func (r *Robot) Work() { /*...*/ }

// Functions accept minimal interfaces
func PayEmployee(p Payable) { /*...*/ }  // Only humans
func WorkWithAny(w Workable) { /*...*/ } // Both humans and robots
```

**Pattern**: Go's standard library exemplifies this (`io.Reader`, `io.Writer`, etc.).

## 5. Dependency Inversion Principle

High-level modules shouldn't depend on low-level modules. Both should depend on abstractions.

### The Problem

```go
type MySQLDB struct{}
func (db *MySQLDB) Save(data string) error { /*...*/ }

type UserService struct {
    db *MySQLDB // Direct dependency on concrete type
}

func (s *UserService) CreateUser(name string) error {
    return s.db.Save(name) // Tightly coupled, can't switch databases
}
```

Changing database implementation requires modifying `UserService`. Testing with a mock database is difficult.

### The Solution

```go
type Database interface {
    Save(data string) error
}

type UserService struct {
    db Database // Depends on abstraction
}

func NewUserService(db Database) *UserService {
    return &UserService{db: db}
}

// Works with any Database implementation
service := NewUserService(&MySQLDB{})
service := NewUserService(&PostgresDB{})
service := NewUserService(&MockDB{}) // For testing
```

**Pattern**: Constructor injection enables testing and flexibility.

## SOLID Principles at a Glance

```
SRP  → One responsibility per type
OCP  → Extend through interfaces, not modification
LSP  → Implementations honor contracts
ISP  → Small, focused interfaces
DIP  → Inject abstractions, not concrete types
```

## Trade-offs and Applicability

| Principle | Cost | Benefit | When to Apply |
|-----------|------|---------|---------------|
| **SRP** | More files/types | Easier to test and modify | Always |
| **OCP** | Requires design | Safe extensions | Anticipated change points |
| **LSP** | Careful design | Predictable behavior | Public interfaces |
| **ISP** | Interface proliferation | Flexible composition | Many implementations |
| **DIP** | Constructor complexity | Testability, decoupling | Service layer code |

## Real-world Application: Payment Processing

```
Domain Model (SRP)
└── PaymentProcessor (OCP)
    ├── CreditCard (LSP + DIP)
    ├── PayPal
    └── Crypto

Logger (ISP - single method)
├── Log()

Repository (DIP - injected)
├── Save()
└── Fetch()
```

Each payment method extends processor without modifying existing code. Small interfaces keep components focused. Dependency injection enables testing with mock database and logger.

## Go-Specific Patterns

- **Implicit Interfaces**: Duck typing makes ISP natural (`io.Reader`, `io.Writer`)
- **Composition over Inheritance**: No inheritance means SRP is the default
- **Struct Embedding**: Enables OCP through composition
- **Constructor Functions**: Standard pattern for DIP (`NewService(dep)`)
- **Table-Driven Tests**: SRP makes this natural

## Common Mistakes

- Over-engineering: Applying SOLID to trivial code
- Ignoring LSP: Implementations that violate interface contracts
- Fat Interfaces: Creating catch-all interfaces
- Circular Dependencies: Improper DIP implementation
- Premature Generalization: Extracting abstractions before patterns emerge

## Best Practices

1. **Start Concrete**: Write working code, extract interfaces when patterns emerge
2. **Accept Interfaces, Return Structs**: Caller provides abstraction, function returns concrete type
3. **Minimize Interface Size**: One or two methods per interface
4. **Test-Driven Design**: SOLID principles naturally emerge from writing testable code
5. **Refactor Incrementally**: Apply principles as complexity grows

## Explanation

SOLID principles in Go emerge naturally from Go's philosophy: composition over inheritance, implicit interfaces, and simple explicit design. Unlike languages requiring careful OOP hierarchy design, Go encourages discovering abstractions through concrete implementations.

Start with straightforward code. When you notice duplication or multiple reasons to change a type, extract responsibilities. When you need variants, define an interface. When testing becomes difficult, inject dependencies. This bottom-up approach yields cleaner designs than imposing SOLID top-down.

The Go standard library (`io`, `net`, `encoding`) demonstrates SOLID in practice. Study these packages to understand how small, focused interfaces and composition create flexible, maintainable systems without the overhead of enterprise OOP frameworks.
