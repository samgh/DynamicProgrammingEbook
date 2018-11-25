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


class TargetSum(object):

    def naive_target_sum(nums, T):
        """
        Naive brute force solution. Find every possible combination
        """
        return TargetSum.__naive_target_sum(nums, T, 0, 0)

    def __naive_target_sum(nums, T, i, cur_sum):
        #  When we've gone through every item, see if we've reached our target sum
        if i == len(nums):
            return int(cur_sum == T)

        # Combine the number of possibilities by adding and subtracting the
        # current value
        return TargetSum.__naive_target_sum(nums, T, i+1, cur_sum + nums[i]) + TargetSum.__naive_target_sum(nums, T, i+1, cur_sum - nums[i])

    def top_down_target_sum(nums, T):
        """
        Top down dynamic programming solution. Like with 0-1 Knapsack, we use a 
        hash map to save on space

        Map: i -> sum -> value
        """

        cache = {}
        return TargetSum.__top_down_target_sum(nums, T, 0, 0, cache)

    def __top_down_target_sum(nums, T, i, cur_sum, cache):

        if i == len(nums):
            return int(cur_sum == T)

        # Check the cache and return value if we get a hit
        if i not in cache:
            cache[i] = {}

        cached = cache[i].get(cur_sum)
        if cached:
            return cached

        # If we didn't hit in the cache, compute the value and store to cache
        return_value = TargetSum.__top_down_target_sum(
            nums, T, i+1, cur_sum + nums[i], cache) + TargetSum.__top_down_target_sum(nums, T, i+1, cur_sum - nums[i], cache)

        cache[i][cur_sum] = return_value

        return return_value

    def bottom_up_target_sum(nums, T):
        """
        Bottom up dynamic programming solution
        """

        # Our cache has to range from -sum(nums) to sum(nums), so we offset
        # everything by sum
        _sum = sum(nums)

        cache = [[0]*(2*_sum + 1) for _ in range(len(nums)+1)]

        if _sum == 0:
            return 0

        # Initialize i=0, T=0
        cache[0][_sum] = 1

        # Iterate over the previous row and update the current row
        for i in range(1, len(nums)+1):
            for j in range(2*_sum + 1):
                prev = cache[i-1][j]
                if prev != 0:
                    cache[i][j - nums[i-1]] += prev
                    cache[i][j + nums[i-1]] += prev

        return cache[len(nums)][_sum + T]


class TestKnapsack(unittest.TestCase):

    def setUp(self):
        self.testcases = [
            ([], 1, 0), ([1, 1, 1, 1, 1], 3, 5), ([1, 1, 1], 1, 3)]

    def test_naive_target_sum(self):
        for nums, value, expected in self.testcases:
            with self.subTest(value=(nums, value)):
                self.assertEqual(
                    TargetSum.naive_target_sum(nums, value), expected)

    def test_top_down_target_sum(self):
        for nums, value, expected in self.testcases:
            with self.subTest(value=(nums, value)):
                self.assertEqual(
                    TargetSum.top_down_target_sum(nums, value), expected)

    def test_bottom_up_target_sum(self):
        for nums, value, expected in self.testcases:
            with self.subTest(value=(nums, value)):
                self.assertEqual(
                    TargetSum.bottom_up_target_sum(nums, value), expected)


if __name__ == '__main__':
    unittest.main()
