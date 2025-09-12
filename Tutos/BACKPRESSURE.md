# Backpressure in Go

Backpressure prevents a fast producer from overwhelming a slow consumer by controlling data flow. In Go, use buffered channels and `select` to signal or block when buffers fill, forcing the producer to wait.

## Key Concept

- **Producer**: Sends data to a channel.
- **Consumer**: Reads from the channel.
- **Backpressure**: Occurs when channel buffer is full; send blocks, slowing producer.

## Simple Example with Select
```go
package main

import (
	"fmt"
	"time"
)

func producer(ch chan<- int) {
	for i := 0; i < 10; i++ {
		select {
		case ch <- i: // Try to send; succeeds if buffer has space
			fmt.Println("Produced:", i)
		default: // Backpressure: buffer full, skip or wait
			fmt.Println("Backpressure: buffer full, waiting...")
			time.Sleep(100 * time.Millisecond) // Simulate wait
			i-- // Retry same item
		}
	}
	close(ch) // Signal end
}

func consumer(ch <-chan int) {
	for val := range ch {
		fmt.Println("Consumed:", val)
		time.Sleep(200 * time.Millisecond) // Slow consumer
	}
}

func main() {
	ch := make(chan int, 3) // Small buffer for backpressure demo
	go producer(ch)
	consumer(ch)
}
```

## Explanation

- **Buffer size 3**: Producer sends up to 3 items without blocking.
- **Select with default**: If send blocks (buffer full), default executes, simulating backpressure by retrying or pausing.
- **Consumer delay**: Forces backpressure, as producer can't send faster.
- **Result**: Producer slows down, preventing overflow. Use `select` with timeouts or other cases for advanced control (e.g., graceful shutdown).