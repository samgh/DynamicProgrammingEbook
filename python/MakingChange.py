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


class MakingChange(object):

    def __init__(self, coins):
        self.coins = coins

    def greedy_making_change(self, c):
        """    
        Greedy algorithm. Take the largest coin possible each time. Doesn't work
        for all coin systems. We also assume that the coins are in descending 
        order
        """
        total_coins = 0
        # Remove the largest coin from c that doesn't make c negative
        for coin in self.coins:
            while c - coin >= 0:
                total_coins += 1
                c -= coin
        return total_coins

    def optimal_greedy_making_change(self, c):
        """
        Optimized greedy algorithm. By using mods, we can solve this in constant
        time but this solution has the same limitations
        """
        total_coins = 0
        # Find how many of each coin can go into the remaining total
        for coin in self.coins:
            total_coins += c // coin
            c %= coin
        return total_coins

    def naive_making_change(self, c):
        """
        Brute force solution. Go through every possible combination of coins that
        sum up to c to find the minimum number
        """
        if c == 0:
            return 0

        min_coins = float('inf')

        # Try removing each coin from the total and see how many more coins
        # are required
        for coin in self.coins:
            # Skip a coin if it's value is greater than the amount remaining
            if c - coin >= 0:
                cur_min_coins = self.naive_making_change(c - coin)
                min_coins = min(min_coins, cur_min_coins)

        # Our recursive call removes one coin from the amount, so add it back
        return min_coins + 1

    def top_down_making_change_optimized(self, c):
        """
        Top down dynamic solution. Cache the values as we compute them
        """

        cache = [-1]*(c+1)
        cache[0] = 0

        return self.__top_down_making_change_optimized(c, cache)

    def __top_down_making_change_optimized(self, c, cache):
        # Return the value if it's in the cache
        if cache[c] >= 0:
            return cache[c]

        min_coins = float('inf')

        # Try removing each coin from the total and see how many more coins
        # are required
        for coin in self.coins:
            # Skip a coin if it's value is greater than the amount remaining
            if c - coin >= 0:
                cur_min_coins = self.__top_down_making_change_optimized(
                    c - coin, cache)
                min_coins = min(min_coins, cur_min_coins)

        # Save the value into the cache
        cache[c] = min_coins + 1
        return cache[c]

    def bottom_up_making_change(self, c):
        cache = [0]*(c+1)
        for i in range(1, c+1):
            min_coins = float('inf')

            # Try removing each coin from the total and see which requires
            # the fewest additional coins

            for coin in self.coins:
                if i - coin >= 0:
                    cur_min_coins = cache[i-coin] + 1
                    min_coins = min(min_coins, cur_min_coins)

            cache[i] = min_coins
        return cache[c]


class TestMakingChange(unittest.TestCase):

    def setUp(self):
        self.american_coins = [25, 10, 5, 1]
        self.random_coins = [10, 6, 1]

        self.testcases = [(self.american_coins, 1, 1), (self.american_coins, 6, 2), (self.american_coins, 47, 5), (
            self.random_coins, 1, 1), (self.random_coins, 8, 3), (self.random_coins, 11, 2), (self.random_coins, 12, 2)]

    def test_naive_making_change(self):
        for coins, value, expected in self.testcases:
            making_change = MakingChange(coins)
            with self.subTest(value=(coins, value)):
                self.assertEqual(
                    making_change.naive_making_change(value), expected)

    def test_top_down_making_change_optimized(self):
        for coins, value, expected in self.testcases:
            making_change = MakingChange(coins)
            with self.subTest(value=(coins, value)):
                self.assertEqual(
                    making_change.top_down_making_change_optimized(value), expected)

    def test_bottom_up_making_change(self):
        for coins, value, expected in self.testcases:
            making_change = MakingChange(coins)
            with self.subTest(value=(coins, value)):
                self.assertEqual(
                    making_change.bottom_up_making_change(value), expected)


if __name__ == '__main__':
    unittest.main()
