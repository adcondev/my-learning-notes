# Test Patterns in Go

Go testing follows a hierarchy of patterns from isolated unit tests to full system integration. Each pattern serves different purposes: Unit tests verify individual functions, Mocks isolate dependencies, Fakes provide working implementations, and E2E tests validate complete workflows.

## Key Concepts

- **Unit Tests**: Test individual functions in isolation with minimal dependencies.
- **Mock**: Simulate dependencies with predetermined responses for specific test scenarios.
- **Fake**: Working implementation with simplified behavior (e.g., in-memory database).
- **E2E (End-to-End)**: Test complete user workflows through the entire system.
- **Integration**: Test interaction between multiple components or external systems.

## Test Patterns Hierarchy

```go
package main

import (
    "errors"
    "fmt"
    "testing"
)

// UserService represents our service layer
type UserService struct {
    repo UserRepository
}

type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
}

// UserRepository interface for dependency injection
type UserRepository interface {
    GetUser(id int) (*User, error)
    SaveUser(user *User) error
}

// Real implementation (production code)
type DatabaseRepository struct{}

func (r *DatabaseRepository) GetUser(id int) (*User, error) {
    // Real database call would go here
    return &User{ID: id, Name: "Real User"}, nil
}

func (r *DatabaseRepository) SaveUser(user *User) error {
    // Real database save would go here
    return nil
}

// Service method to test
func (s *UserService) GetUserName(id int) (string, error) {
    if id <= 0 {
        return "", errors.New("invalid user ID")
    }
    user, err := s.repo.GetUser(id)
    if err != nil {
        return "", err
    }
    return user.Name, nil
}
```

## 1. Unit Tests (Table-Driven)

```go
func TestUserService_GetUserName_Unit(t *testing.T) {
    tests := []struct {
        name     string
        userID   int
        mockUser *User
        mockErr  error
        expected string
        wantErr  bool
    }{
        {"valid user", 1, &User{ID: 1, Name: "John"}, nil, "John", false},
        {"user not found", 2, nil, errors.New("user not found"), "", true},
        {"invalid ID", -1, nil, nil, "", true},
        {"zero ID", 0, nil, nil, "", true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            // Use mock repository
            mockRepo := &MockUserRepository{
                user: tt.mockUser,
                err:  tt.mockErr,
            }
            service := &UserService{repo: mockRepo}

            result, err := service.GetUserName(tt.userID)

            // Check error expectation
            if (err != nil) != tt.wantErr {
                t.Errorf("GetUserName() error = %v, wantErr %v", err, tt.wantErr)
                return
            }

            // Check result
            if result != tt.expected {
                t.Errorf("GetUserName() = %v, want %v", result, tt.expected)
            }
        })
    }
}
```

## 2. Mock Implementation

```go
// MockUserRepository for unit testing
type MockUserRepository struct {
    user *User
    err  error
}

func (m *MockUserRepository) GetUser(id int) (*User, error) {
    return m.user, m.err
}

func (m *MockUserRepository) SaveUser(user *User) error {
    return m.err
}

// Test mock behavior specifically
func TestMockUserRepository(t *testing.T) {
    mock := &MockUserRepository{
        user: &User{ID: 1, Name: "Mock User"},
        err:  nil,
    }

    user, err := mock.GetUser(1)
    if err != nil {
        t.Errorf("Mock should not return error: %v", err)
    }
    if user.Name != "Mock User" {
        t.Errorf("Mock returned wrong user: %v", user)
    }
}
```

## 3. Fake Implementation

```go
// FakeUserRepository for integration testing
type FakeUserRepository struct {
    users map[int]*User
    nextID int
}

func NewFakeUserRepository() *FakeUserRepository {
    return &FakeUserRepository{
        users: make(map[int]*User),
        nextID: 1,
    }
}

func (f *FakeUserRepository) GetUser(id int) (*User, error) {
    user, exists := f.users[id]
    if !exists {
        return nil, errors.New("user not found")
    }
    return user, nil
}

func (f *FakeUserRepository) SaveUser(user *User) error {
    if user.ID == 0 {
        user.ID = f.nextID
        f.nextID++
    }
    f.users[user.ID] = user
    return nil
}

// Test fake with stateful behavior
func TestFakeUserRepository_Integration(t *testing.T) {
    fake := NewFakeUserRepository()
    service := &UserService{repo: fake}

    // Save a user
    user := &User{Name: "Test User"}
    err := fake.SaveUser(user)
    if err != nil {
        t.Fatalf("Failed to save user: %v", err)
    }

    // Retrieve user name
    name, err := service.GetUserName(user.ID)
    if err != nil {
        t.Fatalf("Failed to get user name: %v", err)
    }

    if name != "Test User" {
        t.Errorf("Expected 'Test User', got '%s'", name)
    }
}
```

## 4. E2E Test Example

```go
// E2E test would typically test through HTTP endpoints
func TestUserAPI_E2E(t *testing.T) {
    // Skip in unit test runs
    if testing.Short() {
        t.Skip("Skipping E2E test in short mode")
    }

    tests := []struct {
        name           string
        setupUser      *User
        requestUserID  string
        expectedStatus int
        expectedName   string
    }{
        {"existing user", &User{Name: "John Doe"}, "1", 200, "John Doe"},
        {"non-existent user", nil, "999", 404, ""},
        {"invalid user ID", nil, "abc", 400, ""},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            // Setup: Start test server with real database
            server := setupTestServer()
            defer server.Close()

            // Setup test data
            if tt.setupUser != nil {
                createTestUser(server.URL, tt.setupUser)
            }

            // Execute: Make HTTP request
            resp, err := makeGetUserRequest(server.URL, tt.requestUserID)
            if err != nil {
                t.Fatalf("Request failed: %v", err)
            }
            defer resp.Body.Close()

            // Verify status code
            if resp.StatusCode != tt.expectedStatus {
                t.Errorf("Expected status %d, got %d", tt.expectedStatus, resp.StatusCode)
            }

            // Verify response content if success expected
            if tt.expectedStatus == 200 {
                // Parse and verify response body
                // Implementation would depend on your API format
            }
        })
    }
}

// Helper functions for E2E tests
func setupTestServer() *httptest.Server {
    // Implementation would start your actual server
    // with test database configuration
    return nil
}

func createTestUser(baseURL string, user *User) {
    // Implementation would make POST request to create user
}

func makeGetUserRequest(baseURL, userID string) (*http.Response, error) {
    // Implementation would make GET request
    return nil, nil
}
```

## Pattern Selection Guide

| Test Type | Use When | Pros | Cons |
|-----------|----------|------|------|
| **Unit** | Testing individual functions | Fast, isolated, reliable | Limited scope |
| **Mock** | Isolating external dependencies | Predictable, fast | Doesn't test real integration |
| **Fake** | Testing with simple real behavior | More realistic than mocks | More complex setup |
| **E2E** | Validating complete workflows | Tests real user scenarios | Slow, brittle, hard to debug |

## Explanation

- **Unit Tests**: Use table-driven tests with mocks to verify business logic in isolation.
- **Mocks**: Predetermined responses for specific test scenarios; use when you need exact control over dependency behavior.
- **Fakes**: Working implementations with real but simplified behavior; ideal for integration tests that need stateful interactions.
- **E2E Tests**: Test complete user workflows through actual system interfaces; run with `go test` (skip with `go test -short` for faster builds).
- **Best Practice**: Write mostly unit tests (fast feedback), some integration tests (realistic scenarios), few E2E tests (critical paths only).