package main

import (
	"context"
	"fmt"
	"log"
	"math"
	"os"

	"github.com/google/generative-ai-go/genai"
	"github.com/joho/godotenv"
	"google.golang.org/api/option"
)

func LinearSearch(arr []int, target int) int {
	for i, v := range arr {
		if target == v {
			return i
		}
	}
	return -1
}

func BubbleSort(arr []int) {
	n := len(arr)              // Get array length
	for i := 0; i < n-1; i++ { // Outer loop
		swap := false                // Track if elements were swapped
		for j := 0; j < n-i-1; j++ { // Compare adjacent elements
			if arr[j] > arr[j+1] { // Swap if out of order
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap = true
			}
		}
		if !swap { // No swaps means already sorted
			break
		}
	}
}

func Chapter2() {
	const x = 20
	var i int = x
	var f float64 = x
	fmt.Println(i, f)
	var b byte = math.MaxUint8
	var smallI int32 = math.MaxInt32
	var bigI uint64 = math.MaxUint64
	b += 1
	smallI += 1
	bigI += 1
	fmt.Println(b, smallI, bigI)
	arr := []int{64, 34, 25, 12, 22, 11, 90}
	BubbleSort(arr)
	fmt.Println("Sorted array:", arr)
	fmt.Println(LinearSearch(arr, 90))
}

type Kid struct {
	Age     int `json:"age"`
	Candies int `json:"candies"`
}

func main() {
	if err := godotenv.Load(); err != nil {
		log.Println("Warning: No .env file found")
	}
	apiKey := os.Getenv("GEMINI_API_KEY")
	ctx := context.Background()
	client, err := genai.NewClient(ctx, option.WithAPIKey(apiKey))
	if err != nil {
		log.Fatal(err)
	}
	model := client.GenerativeModel("gemini-2.5-flash")
	result, err := model.GenerateContent(
		ctx,
		genai.Text("Explain how AI works in a few words"),
	)
	if err != nil {
		log.Fatal(err)
	}
	if len(result.Candidates) > 0 && len(result.Candidates[0].Content.Parts) > 0 {
		for _, part := range result.Candidates[0].Content.Parts {
			fmt.Println(part)
		}
	} else {
		fmt.Println("Sin respuesta")
	}
}
