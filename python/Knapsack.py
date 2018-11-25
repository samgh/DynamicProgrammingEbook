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


class Item(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class Knapsack(object):

    def naive_knapsack(items, W):
        return Knapsack.__naive_knapsack(items, W, 0)

    def __naive_knapsack(items, W, i):
        # If we've gone through all the items, return
        if i == len(items):
            return 0

        # If the item is too big to fill the remaining space, skip it
        if W - items[i].weight < 0:
            return Knapsack.__naive_knapsack(items, W, i+1)

        # Find the maximum of including and not including the current item
        return max(Knapsack.__naive_knapsack(items, W - items[i].weight, i+1) + items[i].value, Knapsack.__naive_knapsack(items, W, i+1))

    def top_down_knapsack(items, W):
        cache = {}
        return Knapsack.__top_down_knapsack(items, W, 0, cache)

    def __top_down_knapsack(items, W, i, cache):
        if i == len(items):
            return 0

        # Check if the value is in the cache
        if i not in cache:
            cache[i] = {}

        cached = cache[i].get(W)
        if cached:
            return cached

        # If not, compute the item and add it to the cache
        if W - items[i].weight < 0:
            # exclude item
            return_value = Knapsack.__top_down_knapsack(items, W, i+1, cache)
        else:
            return_value = max(Knapsack.__top_down_knapsack(
                items, W - items[i].weight, i+1, cache) + items[i].value, Knapsack.__top_down_knapsack(items, W, i+1, cache))

        cache[i][W] = return_value

        return return_value

    def bottom_up_knapsack(items, W):
        """
        Iterative bottom up solution
        """
        cache = [[0]*(W+1) for _ in range(len(items) + 1)]

        # For each item and weight, compute the max value of the items up to
        # that item that doesn't go over W weight

        for i in range(1, len(items)+1):
            for j in range(W+1):
                if items[i-1].weight > j:
                    cache[i][j] = cache[i-1][j]
                else:
                    cache[i][j] = max(cache[i-1][j], cache[i-1]
                                      [j-items[i-1].weight] + items[i-1].value)

        return cache[len(items)][W]

    def bottom_up_knapsack_optimized(items, W):
        """
        Optimized bottom up solution with 1D cache. Same as before but only save
        the cache of i-1 and not all values of i
        """

        cache = [0]*(W+1)

        for item in items:
            new_cache = [0]*(W+1)
            for j in range(W+1):
                if item.weight > j:
                    new_cache[j] = cache[j]
                else:
                    new_cache[j] = max(
                        cache[j], cache[j-item.weight] + item.value)

            cache = new_cache

        return cache[W]


class TestKnapsack(unittest.TestCase):

    def setUp(self):
        self.testcases = [([], 0, 0), ([Item(4, 5), Item(1, 8), Item(2, 4), Item(3, 0), Item(2, 5), Item(
            2, 3)], 3, 13), ([Item(4, 5), Item(1, 8), Item(2, 4), Item(3, 0), Item(2, 5), Item(2, 3)], 8, 20)]

    def test_naive_knapsack(self):
        for items, weight, expected in self.testcases:
            with self.subTest(value=(items, weight)):
                self.assertEqual(
                    Knapsack.naive_knapsack(items, weight), expected)

    def test_top_down_knapsack(self):
        for items, weight, expected in self.testcases:
            with self.subTest(value=(items, weight)):
                self.assertEqual(
                    Knapsack.top_down_knapsack(items, weight), expected)

    def test_bottom_up_knapsack(self):
        for items, weight, expected in self.testcases:
            with self.subTest(value=(items, weight)):
                self.assertEqual(
                    Knapsack.bottom_up_knapsack(items, weight), expected)

    def test_bottom_up_knapsack_optimized(self):
        for items, weight, expected in self.testcases:
            with self.subTest(value=(items, weight)):
                self.assertEqual(
                    Knapsack.bottom_up_knapsack_optimized(items, weight), expected)


if __name__ == '__main__':
    unittest.main()
