# **Chapter 2: Predeclared Types and Declarations**

> *Based on "Learning Go (2nd Edition)"*  
> **Objective**: Understand Go’s built-in types, variable declarations, and constants for more expressive and error-free code.

---

## **Table of Contents**

1. [Introduction](#introduction)  
2. [Predeclared Types](#predeclared-types)  
   - [Zero Value](#zero-value)  
   - [Literals](#literals)  
   - [Booleans](#booleans)  
   - [Numeric Types](#numeric-types)  
3. [Strings and Runes](#strings-and-runes)  
4. [Explicit Type Conversion](#explicit-type-conversion)  
5. [var vs :=](#var-vs-)  
6. [Using const](#using-const)  
   - [Typed and Untyped Constants](#typed-and-untyped-constants)  
7. [Unused Variables](#unused-variables)  
8. [Naming Variables and Constants](#naming-variables-and-constants)  
9. [Summary and Quick Revision](#summary-and-quick-revision)  
   - [Extra Tips](#extra-tips)  
   - [Best Practices](#best-practices)  
   - [Common Pitfalls](#common-pitfalls)  
   - [Interview Questions](#interview-questions)  

---

## **Introduction**

Go provides a rich set of **predeclared types** (booleans, integers, floats, strings, runes) and straightforward **declaration rules**. Although these concepts exist in most languages, Go’s approach emphasizes clarity and simplicity:  
- **Zero values** to avoid null references or uninitialized variables.  
- **Untyped literals** to allow flexible assignment.  
- **Strict declaration rules** to encourage explicit code.

---

## **Predeclared Types**

Go ships with many built-in types that streamline everyday coding tasks, commonly grouped into:
1. **Boolean** (*bool*)
2. **Numeric** (*int, float64, etc.*)
3. **String** and **Rune**

### **Zero Value**

In Go, declared variables that aren’t initialized receive a default **zero value**:  
- **bool** → `false`  
- **numeric types** → `0` (e.g., `int`, `float64`)  
- **string** → `""` (empty string)  
- **pointer** → `nil`  

> **Why Zero Value?**  
> Reduces the chance of runtime errors from uninitialized variables.

---

### **Literals**

A literal is a fixed value in source code. Common literal forms:

- **Integer literals**:
  ```go
  var dec int = 10   // decimal
  var bin int = 0b1010   // binary
  var oct int = 0o12     // octal
  var hex int = 0xA      // hexadecimal
  ```

- **Floating-point literals**:
  ```go
  var f1 float64 = 10.0    // decimal
  var f2 float64 = 1.0e+10 // scientific notation
  var f3 float64 = 0x1p+0  // hexadecimal floating-point
  ```

- **Rune literals** (single quotes):
  ```go
  var r1 rune = 'A'       // Unicode character
  var r2 rune = '\101'    // octal
  var r3 rune = '\x41'    // hex
  var r4 rune = '\u0041'  // 16-bit Unicode
  var r5 rune = '\U00000041' // 32-bit Unicode
  ```

- **String literals**:
  - **Interpreted** (double quotes `" "`):
    ```go
    var s1 string = "hello\nworld"
    ```
  - **Raw** (backquotes `` ` ` ``):
    ```go
    var s2 string = `hello\nworld`
    ```
  Raw strings keep all special characters (except the backquote) literally.

---

### **Booleans**

- Declared via the `bool` type.
- Possible values: `true` or `false`.
- Zero value is `false`.

```go
var flag bool      // defaults to false
var isAwesome = true
```

> **Reminder**: Go does **not** allow implicit truthiness or falsiness (like in some scripting languages). You must use comparison operators to obtain a boolean value.

---

### **Numeric Types**

Go has a rich set of numeric types to suit various performance and memory constraints.

#### **Integers**

Signed and unsigned integers in one to eight bytes:

| **Type** | **Size**     | **Range (Signed)**                    |
|----------|--------------|---------------------------------------|
| `int8`   | 1 byte (8 bits)  | -128 to 127                        |
| `int16`  | 2 bytes (16 bits) | -32768 to 32767                   |
| `int32`  | 4 bytes (32 bits) | -2,147,483,648 to 2,147,483,647    |
| `int64`  | 8 bytes (64 bits) | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `uint8`  | 1 byte (8 bits)  | 0 to 255                           |
| `uint16` | 2 bytes (16 bits) | 0 to 65535                        |
| `uint32` | 4 bytes (32 bits) | 0 to 4,294,967,295                |
| `uint64` | 8 bytes (64 bits) | 0 to 18,446,744,073,709,551,615    |

**Special integer names** in Go:
- `byte` (alias for `uint8`)
- `int` (typically 32-bit or 64-bit depending on platform)
- `uint` (same size as `int`, but unsigned)

> **Zero value** for integers is `0`.

**Common operators**:
- Arithmetic: `+ - * / %`  
- Combination assignments: `+=, -=, *=, /=, %=`
- Comparisons: `==, !=, >, >=, <, <=`
- Bitwise: `<<, >>, &, |, ^, &^` (+ combo assignments)

Example:
```go
var x int = 10
x += 5   // 15
x <<= 2  // 60
```

#### **Floating-Point**

Two primary floating-point types: `float32` and `float64`.

| **Type**   | **Size**    | **Range**         |
|------------|-------------|-------------------|
| `float32`  | 4 bytes     | ±1.18e-38 to ±3.4e+38  |
| `float64`  | 8 bytes     | ±2.23e-308 to ±1.8e+308|

- Zero value: `0.0`
- Defaults: Unannotated floating literals become `float64`.

> **Infinity & NaN**: Dividing a nonzero float by `0` → `±Inf`. Dividing `0.0` by `0.0` → `NaN`.

---

## **Strings and Runes**

- **String** zero value is the empty string `""`.
- Strings are **immutable**; you can’t modify them in place.
- **Rune** is an alias for `int32`; default type for a rune literal (`'A'`) is `rune`.

```go
var c rune = 'A'    // recommended
var d int32 = 'B'   // valid but confusing
```

Strings support:
- Equality checks `==` and `!=`
- Lexicographical comparisons `>`, `<`, `>=`, `<=`
- Concatenation with `+`

---

## **Explicit Type Conversion**

Go **does not** allow automatic type promotions. You must convert explicitly:

```go
var x int = 10
var y float64 = 20.0

// Convert x to float64
var sum1 float64 = float64(x) + y

// Convert y to int
var sum2 int = x + int(y)
```

> **No Implicit Truthiness**: You cannot do `if x { ... }` to check if `x` is nonzero. Instead use `if x != 0 { ... }`.

---

## **var vs :=**

Two primary ways to declare variables:

1. **`var`** declarations:
   ```go
   var a int = 10        // explicit type
   var b = 10            // inferred type
   var c int             // zero value
   var d, e int = 10, 20 // multiple variables
   var (
       f   int
       g   int = 20
       h       = "hello"
   )
   ```

2. **`:=`** short declaration (only **inside** functions):
   ```go
   x := 10
   y, z := 20, "hello"
   ```

**Preferred Usage**:
- Use `:=` **within functions** for brevity.
- Use `var` **outside functions** (package-level) because `:=` is disallowed there.
- Multi-variable declarations with `:=` are often used for **function return values** or the **comma ok idiom**.

---

## **Using const**

Constants (`const`) define **immutable** named values known at compile time. They **cannot** be the result of runtime computations.

```go
const a = 10    // allowed
x := 10
y := 20
const z = x + y // compile error - x + y is runtime
```

### **Typed and Untyped Constants**

- **Untyped constant**: No fixed type, but a default type is inferred if needed.
- **Typed constant**: Only assignable to variables of the same type.

```go
const x = 10        // untyped
var y int = x       // legal
var z float64 = x   // also legal

const typedX int = 10
// typedX can only assign directly to int variables
```

---

## **Unused Variables**

Go enforces that **every declared local variable must be read** at least once; otherwise, it’s a compile-time error:

```go
func main() {
    x := 10      // assigned but not read
    x = 20       // updated
    fmt.Println(x)  // read -> OK
    x = 30       // assigned but never read
}
```

- **Package-level** variables can remain unused without compile-time errors.
- **Unused constants** are allowed, as they have no runtime footprint.

---

## **Naming Variables and Constants**

- Must start with a letter or underscore (`_`); can contain letters, digits, underscores.
- **CamelCase** is idiomatic in Go.
- Smaller scopes → shorter names (`i`, `j`). Larger scopes → more descriptive (`indexCounter`).

> **Guideline**: If a short name confuses you, your function or block might be doing too much. Keep scopes small, names meaningful.

---

## **Summary and Quick Revision**

1. **Types**: Mastering booleans, numeric types, runes, and strings helps avoid confusion.  
2. **Zero Values**: Avoids null references; uninitialized variables default to a safe zero value.  
3. **Literals**: Integers, floats, runes, strings are flexible. Untyped allows easy usage across expressions.  
4. **Conversions**: Go is explicit about type conversion, reinforcing readability.  
5. **Declarations**: `var` (package-level) vs `:=` (function-level).  
6. **Constants**: Compile-time named literals; not for runtime expressions.  
7. **Naming**: Use descriptive names in broader scopes; short names for tight scopes or idiomatic patterns.

### **Extra Tips**

- **Use `float64`** by default for floating-point calculations to avoid subtle precision issues.  
- **Remember** that rune is just `int32`—useful for storing Unicode code points.  
- **Practice** bitwise operations (`&`, `|`, `^`) for performance-critical tasks like cryptography or image processing.

### **Best Practices**

- Favor **short declarations** (`:=`) for local variables; it improves readability.  
- Keep **constants untyped** where possible for greater flexibility.  
- Use **package-level variables** sparingly; prefer function-level or smaller-scope variables.

### **Common Pitfalls**

1. **Forgetting to read a local variable** → compile-time error.  
2. **Confusing `=` with `:=`** → `:=` only works inside functions.  
3. **Implicit conversions** → not allowed; must cast explicitly.  
4. **Unused import** or **unused variable** → compiler error in Go.  

### **Interview Questions**

1. **What is a zero value, and how does it help in Go?**  
   Answer: A zero value is the default value assigned to a variable when it is declared but not initialized. It helps avoid null references and provides a safe starting point for variables.
2. **Explain how untyped constants work in Go.**  
   Answer: Untyped constants do not have a fixed type until they are assigned to a variable. They can be used flexibly across different types, and Go infers the appropriate type based on context. 
3. **Why does Go forbid implicit type promotion?**  
   Answer: Go forbids implicit type promotion to maintain clarity and avoid hidden errors. Explicit type conversions make the code more readable and help prevent unintended behavior.
4. **When do you use `var` vs `:=`?**  
   *Answer Hint: Mention scope and usage contexts.*  
5. **What happens if you attempt to do a runtime operation in a constant declaration?**  
   *Answer Hint: It won’t compile; constants must be known at compile time.*  

---

> **Next Steps**: Practice writing short code snippets using these types and declarations. Experiment with constants and the `var` vs. `:=` style in various scopes to understand their usage and limitations.
