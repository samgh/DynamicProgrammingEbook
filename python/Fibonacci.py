#!/usr/bin/env python
# encoding: utf-8

# Copyright (c) 2018 Nikolay Derkach
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest


class Fibonacci(object):
    def naive_fib(n):
        """
        Naive implementation with recursive calls
        """
        if n < 2:
            return n
        return Fibonacci.naive_fib(n-2) + Fibonacci.naive_fib(n-1)

    def top_down_fib_optimized(n):
        """     
        Compute the nth Fibonacci number recursively. Optimized by caching 
        subproblem results
        """

        if n < 2:
            return n

        cache = [-1]*(n+1)
        cache[0] = 0
        cache[1] = 1

        return Fibonacci.__top_down_fib_optimized(n, cache)

    def __top_down_fib_optimized(n, cache):
        if cache[n] >= 0:
            return cache[n]

        cache[n] = Fibonacci.__top_down_fib_optimized(
            n-1, cache) + Fibonacci.__top_down_fib_optimized(n-2, cache)
        return cache[n]

    def bottom_up_fib(n):
        """
        Compute the nth Fibonacci number iteratively
        """

        if n == 0:
            return 0

        cache = [0]*(n+1)
        cache[1] = 1

        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]

    def bottom_up_fib_optimized(n):
        """
        Compute the nth Fibonacci number iteratively with constant space. We only
        need to save the two most recently computed values
        """

        if n < 2:
            return n

        n1, n2 = 1, 0

        for i in range(2, n+1):
            n0 = n1 + n2
            n2 = n1
            n1 = n0

        return n0


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.testcases = [(0, 0), (1, 1), (2, 1), (5, 5), (10, 55)]

    def test_naive(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(Fibonacci.naive_fib(value), expected)

    def test_top_down(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(
                    Fibonacci.top_down_fib_optimized(value), expected)

    def test_bottom_up(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(Fibonacci.bottom_up_fib(value), expected)

    def test_bottom_up_optimized(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(
                    Fibonacci.bottom_up_fib_optimized(value), expected)


if __name__ == '__main__':
    unittest.main()
