# Test Patterns in Go

Go testing follows a hierarchy from isolated unit tests to full system integration. Each pattern serves different purposes: verify individual functions, isolate dependencies, test with realistic behavior, or validate complete workflows.

## Key Concepts

- **Unit Tests**: Test individual functions with mocks
- **Mocks**: Simulate dependencies with predetermined responses
- **Fakes**: Working implementations with simplified behavior
- **Integration Tests**: Multiple components together
- **E2E (End-to-End)**: Complete workflows through actual interfaces

## Test Pyramid

```
       ╱╲
      ╱  ╲  E2E Tests (5%)
     ╱    ╲ Slow, brittle, catches system issues
    ╱──────╲
   ╱        ╲ Integration Tests (15%)
  ╱          ╲ Moderate speed, realistic behavior
 ╱────────────╲
╱              ╲ Unit Tests (80%)
╱________________╲ Fast, isolated, reliable
```

80% unit, 15% integration, 5% E2E for optimal balance.

## Unit Test Pattern: Table-Driven

```go
// Define test cases as data
tests := []struct {
    name     string
    input    int
    expected string
    wantErr  bool
}{
    {"valid case", 5, "result", false},
    {"edge case", 0, "", true},
    {"error case", -1, "", true},
}

// Run each case
for _, tt := range tests {
    t.Run(tt.name, func(t *testing.T) {
        result, err := functionToTest(tt.input)
        
        if (err != nil) != tt.wantErr {
            t.Errorf("got error %v, want %v", err, tt.wantErr)
        }
        if result != tt.expected {
            t.Errorf("got %q, want %q", result, tt.expected)
        }
    })
}
```

**Advantage**: Easy to add cases, clear parameterization

## Mock Pattern

```go
type MockDatabase struct {
    GetFunc func(id string) (string, error)
}

func (m *MockDatabase) Get(id string) (string, error) {
    return m.GetFunc(id)
}

// Use in test
func TestWithMock(t *testing.T) {
    mock := &MockDatabase{
        GetFunc: func(id string) (string, error) {
            return "mocked value", nil
        },
    }
    
    service := NewService(mock)
    result := service.DoSomething()
    // Assert result
}
```

**Trade-off**: Full control, but doesn't test real integration

## Fake Pattern

```go
// Working implementation with simplified behavior
type FakeDatabase struct {
    data map[string]string
}

func (f *FakeDatabase) Get(id string) (string, error) {
    if v, ok := f.data[id]; ok {
        return v, nil
    }
    return "", errors.New("not found")
}

// Use in integration test
func TestIntegration(t *testing.T) {
    fake := &FakeDatabase{
        data: map[string]string{"user1": "alice"},
    }
    
    service := NewService(fake)
    result := service.GetUser("user1")
    
    if result != "alice" {
        t.Errorf("got %q, want %q", result, "alice")
    }
}
```

**Trade-off**: More realistic, but requires implementation

## Test Selection

| Test Type | Speed | Scope | When |
|-----------|-------|-------|------|
| **Unit** | Fast | Single function | Always (majority) |
| **Mock** | Fast | Function with isolated deps | When need exact control |
| **Fake** | Medium | Service + simplified storage | Integration verification |
| **E2E** | Slow | Complete system | Critical user paths only |

## Execution

```bash
# All tests
go test ./...

# Specific test
go test -run TestName ./...

# Without slow tests
go test -short ./...

# With coverage
go test -cover ./...
```

## Best Practices

- **Test Behavior, Not Implementation**: Test what the function does, not how it does it
- **Clear Names**: `TestUserService_CreateUser_ValidInput` is better than `TestCreate`
- **One Assertion Focus**: Each test should verify one thing
- **Parallel Tests**: Use `t.Parallel()` to speed up test runs
- **Fail Fast**: Return early on setup failures

## Explanation

Go's testing philosophy is pragmatic: simple functions, minimal ceremony. The standard testing package lacks assertions library, forcing explicitness about what you're verifying. This is intentional—clear error messages matter more than DSLs.

The pyramid exists because of cost: unit tests are cheap (milliseconds), E2E tests expensive (seconds). Write many fast tests to catch regressions quickly, fewer slow tests for critical paths. This provides fast feedback during development while ensuring core functionality works end-to-end.

Table-driven tests leverage Go's simplicity to scale: adding test cases is just adding rows, no new functions needed. This pattern becomes Go idiom once you've written a few.