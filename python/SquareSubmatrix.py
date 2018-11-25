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


class SquareSubmatrix(object):

    def naive_square_submatrix(arr):
        """
        Brute force solution. From each cell see what is the biggest square
        submatrix for which it is the upper left-hand corner
        """
        max_size = 0
        # Compute recursively for each cell what it is the upper left corner of
        for row in range(len(arr)):
            for column in range(len(arr[row])):
                if arr[row][column]:
                    max_size = max(
                        max_size, SquareSubmatrix.__naive_square_submatrix(arr, row, column))

        return max_size

    def __naive_square_submatrix(arr, row, column):
        # If we get to the bottom or right of the matrix, we can't go any
        # further
        if row == len(arr) or column == len(arr[0]):
            return 0

        # If the cell is False then it is not part of a valid submatrix
        if not arr[row][column]:
            return 0

        # Find the size of the right, bottom, and bottom right submatrices and
        # add 1 to the minimum of those 3 to get the result
        return 1 + min(SquareSubmatrix.__naive_square_submatrix(arr, row+1, column), SquareSubmatrix.__naive_square_submatrix(arr, row, column+1), SquareSubmatrix.__naive_square_submatrix(arr, row+1, column+1))

    def top_down_square_submatrix(arr):
        """
        Top down dynamic programming solution. Cache the values as we compute
        them to avoid repeating computations
        """
        cache = [[0]*len(row) for row in arr]

        max_size = 0
        # Compute recursively for each cell what it is the upper left corner of
        for row in range(len(arr)):
            for column in range(len(arr[row])):
                if arr[row][column]:
                    max_size = max(
                        max_size, SquareSubmatrix.__top_down_square_submatrix(arr, row, column, cache))

        return max_size

    def __top_down_square_submatrix(arr, row, column, cache):
        # If we get to the bottom or right of the matrix, we can't go any
        # further
        if row == len(arr) or column == len(arr[0]):
            return 0

        # If the cell is False then it is not part of a valid submatrix
        if not arr[row][column]:
            return 0

        # If the value is set in the cache return it. Otherwise compute and
        # save to cache
        if cache[row][column]:
            return cache[row][column]

        # Find the size of the right, bottom, and bottom right submatrices and
        # add 1 to the minimum of those 3 to get the result
        cache[row][column] = 1 + min(SquareSubmatrix.__top_down_square_submatrix(arr, row+1, column, cache), SquareSubmatrix.__top_down_square_submatrix(
            arr, row, column+1, cache), SquareSubmatrix.__top_down_square_submatrix(arr, row+1, column+1, cache))

        return cache[row][column]

    def bottom_up_square_submatrix(arr):
        # Initialize cache
        cache = [[0]*len(row) for row in arr]

        max_size = 0

        # Iterate over the matrix to compute all values
        for row in range(len(arr)):
            for column in range(len(arr[row])):
                # If we are in the first row or column then the value is just
                # 1 if that cell is true and 0 otherwise. In other rows and
                # columns, need to look up and to the left
                if row == 0 or column == 0:
                    cache[row][column] = int(arr[row][column])
                else:
                    cache[row][column] = 1 + \
                        min(cache[row-1][column], cache[row]
                            [column-1], cache[row-1][column-1])

                max_size = max(max_size, cache[row][column])

        return max_size


class TestSubMatrix(unittest.TestCase):

    def setUp(self):
        self.testcases = [([[True]], 1), ([[False]], 0), ([[True, True, True, False], [False, True, True, True], [
            True, True, True, True]], 2), ([[True, True, True, True], [False, True, True, True], [True, True, True, True]], 3)]

    def test_naive_making_change(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(
                    SquareSubmatrix.naive_square_submatrix(value), expected)

    def test_top_down_square_submatrix(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(
                    SquareSubmatrix.top_down_square_submatrix(value), expected)

    def test_bottom_up_square_submatrix(self):
        for value, expected in self.testcases:
            with self.subTest(value=value):
                self.assertEqual(
                    SquareSubmatrix.bottom_up_square_submatrix(value), expected)


if __name__ == '__main__':
    unittest.main()
