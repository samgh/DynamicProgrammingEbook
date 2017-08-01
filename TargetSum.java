/*
 * Title: Target Sum
 * Author: Sam Gavis-Hughson
 * Date: 08/01/2017
 * 
 * Given an array of integers, nums and a target value T, find the number of 
 * ways that you can add and subtract the values in nums to add up to T.
 * 
 * eg.
 * nums = {1, 1, 1, 1, 1}
 * target = 3
 * 
 * 1 + 1 + 1 + 1 - 1
 * 1 + 1 + 1 - 1 + 1
 * 1 + 1 - 1 + 1 + 1
 * 1 - 1 + 1 + 1 + 1
 * -1 + 1 + 1 + 1 + 1
 * 
 * targetSum(nums, target) = 5
 * 
 * Execution: javac TargetSum.java && java TargetSum
 */

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TargetSum {
    
    // Naive brute force solution. Find every possible combination
    public static int naiveTargetSum(int[] nums, int T) {
        return naiveTargetSum(nums, T, 0, 0);
    }
    
    // Overloaded recursive function
    private static int naiveTargetSum(int[] nums, int T, int i, int sum) {
        // When we've gone through every item, see if we've reached our target sum
        if (i == nums.length) {
            return sum == T ? 1 : 0;
        }
        
        // Combine the number of possibilites by adding and subtracting the
        // current value
        return naiveTargetSum(nums, T, i+1, sum + nums[i]) + naiveTargetSum(nums, T, i+1, sum - nums[i]);
    }
    
    // Top down dynamic programming solution. Like with 0-1 Knapsack, we use a 
    // HashMap to save on space
    public static int topDownTargetSum(int[] nums, int T) {
        // Map: i -> sum -> value
        Map<Integer, Map<Integer, Integer>> cache = new HashMap<Integer, Map<Integer, Integer>>();
        return topDownTargetSum(nums, T, 0, 0, cache);
    }
    
    // Overloaded recursive function
    private static int topDownTargetSum(int[] nums, int T, int i, int sum, Map<Integer, Map<Integer, Integer>> cache) {
        if (i == nums.length) {
            return sum == T ? 1 : 0;
        }
        
        // Check the cache and return value if we get a hit
        if (!cache.containsKey(i)) cache.put(i, new HashMap<Integer, Integer>());
        Integer cached = cache.get(i).get(sum);
        if (cached != null) return cached;
        
        // If we didn't hit in the cache, compute the value and store to cache
        int toReturn = topDownTargetSum(nums, T, i+1, sum + nums[i], cache) + 
            topDownTargetSum(nums, T, i+1, sum - nums[i], cache);
        cache.get(i).put(sum, toReturn);
        return toReturn;
    }
    
    // Bottom up dynamic programming solution
    public static int bottomUpTargetSum(int[] nums, int T) {
        int sum = 0;
        
        // Our cache has to range from -sum(nums) to sum(nums), so we offset
        // everything by sum
        for (int num : nums) sum += num;
        int[][] cache = new int[nums.length + 1][2 * sum + 1];
        
        if (sum == 0) return 0;
        
        // Initialize i=0, T=0
        cache[0][sum] = 1;
        
        // Iterate over the previous row and update the current row
        for (int i = 1; i <= nums.length; i++) {
            for (int j = 0; j < 2 * sum + 1; j++) {
                int prev = cache[i-1][j]; 
                if (prev != 0) {
                    cache[i][j - nums[i-1]] += prev;
                    cache[i][j + nums[i-1]] += prev;
                }
            }
        }
        
        return cache[nums.length][sum + T];
    }
    
    // Sample testcases
    public static void main(String[] args) {
        (new TestCase(new int[]{}, 1, 0)).run();
        (new TestCase(new int[]{1, 1, 1, 1, 1}, 3, 5)).run();
        (new TestCase(new int[]{1, 1, 1}, 1, 3)).run();
        System.out.println("Passed all test cases");
    }
    
    // Class for defining and running test cases
    private static class TestCase {
        private int[] nums;
        private int target;
        private int output;
        
        private TestCase(int[] nums, int target, int output) {
            this.nums = nums;
            this.target = target;
            this.output = output;
        }
        
        private void run() {
            assert naiveTargetSum(nums, target) == output:
                "naiveTargetSum failed for nums = " + Arrays.toString(nums) + ", target = " + target;
            assert topDownTargetSum(nums, target) == output:
                "topDownTargetSum failed for nums = " + Arrays.toString(nums) + ", target = " + target;
            assert bottomUpTargetSum(nums, target) == output:
                "bottomUpTargetSum failed for nums = " + Arrays.toString(nums) + ", target = " + target;
        }
    }
}