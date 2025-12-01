package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	sum := 0
	for i := 0; i < n; i++ {
		var s, c int
		fmt.Scan(&s, &c)
		sum += s * c
	}

	fmt.Println(sum)
}
