# Exponential Backoff in Go

Exponential backoff is a retry strategy that progressively increases wait time between retries to reduce system load. In Go, implement this pattern to handle transient failures gracefully, particularly in network operations or API calls.

## Key Concepts

- **Initial Delay**: Starting wait time before first retry.
- **Multiplier**: Factor by which delay increases after each failure.
- **Maximum Delay**: Cap on how long delay can become.
- **Jitter**: Random variation added to delay to prevent synchronized retries.
- **Maximum Retries**: Limit on total retry attempts.

## Simple Example with Jitter

```go
package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"
)

func fetchWithBackoff(url string) (*http.Response, error) {
	baseDelay := 100 * time.Millisecond
	maxDelay := 10 * time.Second
	maxRetries := 5
	multiplier := 2.0

	var resp *http.Response
	var err error

	for attempt := 0; attempt <= maxRetries; attempt++ {
		resp, err = http.Get(url)
		
		if err == nil && resp.StatusCode < 500 {
			return resp, nil // Success
		}
		
		if attempt == maxRetries {
			break // Maximum retries reached
		}
		
		// Calculate delay with exponential backoff and jitter
		delay := time.Duration(float64(baseDelay) * 
			pow(multiplier, float64(attempt)))
			
		if delay > maxDelay {
			delay = maxDelay
		}
		
		// Add jitter (±20%)
		jitter := rand.Float64()*0.4 - 0.2 // -20% to +20%
		delay = time.Duration(float64(delay) * (1 + jitter))
		
		fmt.Printf("Attempt %d failed, retrying in %v\n", 
			attempt+1, delay)
		time.Sleep(delay)
	}
	
	return nil, fmt.Errorf("failed after %d attempts: %w", 
		maxRetries, err)
}

// Simple power function to avoid dependency
func pow(base, exp float64) float64 {
	result := 1.0
	for i := 0; i < int(exp); i++ {
		result *= base
	}
	return result
}

func main() {
	// Example usage
	resp, err := fetchWithBackoff("https://api.example.com/resource")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()
	fmt.Println("Success:", resp.Status)
}
```

## Explanation

- **Retry Logic**: Function attempts HTTP request, retrying on failure.
- **Exponential Growth**: Each retry doubles wait time (100ms → 200ms → 400ms → 800ms...).
- **Maximum Cap**: Prevents excessive delays (capped at 10 seconds).
- **Jitter**: Adds randomness (±20%) to prevent thundering herd problem when multiple clients retry simultaneously.
- **Maximum Retries**: Gives up after 5 attempts to prevent infinite retries.

This pattern is ideal for handling transient errors in distributed systems, API calls, or database connections. By gradually backing off and adding randomness, it reduces system load during recovery while still providing resilience against temporary failures.