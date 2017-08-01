/*
 * Title: Fibonacci
 * Author: Sam Gavis-Hughson
 * Date: 08/01/2017
 * 
 * Given an integer n, write a function that will return the nth Fibonacci number.
 * 
 * eg. 
 * fib(0) = 0
 * fib(1) = 1
 * fib(5) = 5
 * fib(10) = 55
 * 
 * Execution: javac Fibonacci.java && java Fibonacci
 */

// We will assume for all solutions that n >= 0 and that int is sufficient
// to hold the result
public class Fibonacci {
    
    // Compute the nth Fibonacci number recursively
    public static int naiveFib(int n) {
        if (n < 2) return n;
        return naiveFib(n-1) + naiveFib(n-2);
    }
    
    // Compute the nth Fibonacci number recursively. Optimized by caching 
    // subproblem results
    public static int topDownFibOptimized(int n) {
        if (n < 2) return n;
        
        // Create cache and initialize to -1
        int[] cache = new int[n+1];
        for (int i = 0; i < cache.length; i++) {
            cache[i] = -1;
        }
        
        // Fill initial values in cache
        cache[0] = 0;
        cache[1] = 1;
        return topDownFibOptimized(n, cache);
    }
    
    // Overloaded private method
    private static int topDownFibOptimized(int n, int[] cache) {
        // If value is set in cache, return
        if (cache[n] >= 0) return cache[n];
        
        // Otherwise compute and add to cache before returning
        cache[n] = topDownFibOptimized(n-1, cache) + topDownFibOptimized(n-2, cache);
        return cache[n];
    }
    
    // Compute the nth Fibonacci number iteratively
    public static int bottomUpFib(int n) {
        if (n == 0) return 0;
        
        // Initialize cache
        int[] cache = new int[n+1];
        cache[1] = 1;
        
        // Fill cache iteratively
        for (int i = 2; i <= n; i++) {
            cache[i] = cache[i-1] + cache[i-2];
        }
        
        return cache[n];
    }
    
    // Compute the nth Fibonacci number iteratively with constant space. We only
    // need to save the two most recently computed values
    public static int bottomUpFibOptimized(int n) {
        if (n < 2) return n;
        int n1 = 1, n2 = 0;
        for (int i = 2; i < n; i++) {
            int n0 = n1 + n2;
            n2 = n1;
            n1 = n0;
        }
        
        return n1 + n2;
    }
    
    // Sample testcases
    public static void main(String[] args) {
        (new TestCase(0, 0)).run();
        (new TestCase(1, 1)).run();
        (new TestCase(2, 1)).run();
        (new TestCase(5, 5)).run();
        (new TestCase(10, 55)).run();
        System.out.println("Passed all test cases");
    }
    
    // Class for defining and running test cases
    private static class TestCase {
        private int input;
        private int output;
        
        private TestCase(int input, int output) {
            this.input = input;
            this.output = output;
        }
        
        private void run() {
            assert naiveFib(input) == output:
                "naiveFib failed for input = " + input;
            assert topDownFibOptimized(input) == output:
                "topDownFibOptimized failed for input = " + input;
            assert bottomUpFib(input) == output:
                "topDownFib failed for input = " + input;
            assert bottomUpFibOptimized(input) == output:
                "topDownFib failed for input = " + input;
        }
    }
}