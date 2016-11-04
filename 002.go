package main

import (
	"fmt"
)

func main() {
	sum := 0
	var x, y int = 1, 2
	for y < 4000000 {
	    if y % 2 == 0 {
	        sum += y	        
	    }
	    next_y := x + y
	    x = y
	    y = next_y
	}
	
	fmt.Println(sum)
}