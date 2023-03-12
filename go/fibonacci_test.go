// @author: Gandharva Shankara Murthy

package _go

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Fib(n int) int {
	if n < 2 {
		return n
	}
	n1 := 1
	n2 := 0
	var n0 int

	for i := 2; i <= n; i++ {
		n0 = n2 + n1
		n1, n2 = n0, n1
	}
	return n0
}

func TestFibonacci(t *testing.T) {
	tests := []struct {
		name string
		no   int
		want int
	}{
		{
			name: "Fib 0",
			no:   0,
			want: 0,
		},
		{
			name: "Fib 1",
			no:   1,
			want: 1,
		},
		{
			name: "Fib 3",
			no:   5,
			want: 5,
		},
		{
			name: "Fib 10",
			no:   10,
			want: 55,
		},
		{
			name: "Fib 50",
			no:   50,
			want: 12586269025,
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := Fib(test.no)
			assert.Equal(t, test.want, got)
		})
	}
}
