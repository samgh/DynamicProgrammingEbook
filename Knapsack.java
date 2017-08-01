/*
 * Title: 0-1 Knapsack
 * Author: Sam Gavis-Hughson
 * Date: 08/01/2017
 * 
 * Given a list of items with values and weights, as well as a max weight, 
 * find the maximum value you can generate from items, where the sum of the 
 * weights is less than or equal to the max.
 * 
 * eg.
 * items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
 * maxWeight = 5
 * knapsack(items, maxWeight) = 22
 * 
 * Execution: javac Knapsack.java && java Knapsack
 */

import java.util.HashMap;
import java.util.Map;

public class Knapsack {
    
    // Public inner class to represent an individual item
    public static class Item {
        int weight;
        int value;
        
        public Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
    
    // Naive brute force solution. Recursively include or exclude each item
    // to try every possible combination
    public static int naiveKnapsack(Item[] items, int W) {
        return naiveKnapsack(items, W, 0);
    }
    
    // Overloaded recursive function
    private static int naiveKnapsack(Item[] items, int W, int i) {
        // If we've gone through all the items, return
        if (i == items.length) return 0;
        // If the item is too big to fill the remaining space, skip it
        if (W - items[i].weight < 0) return naiveKnapsack(items, W, i+1);
        
        // Find the maximum of including and not including the current item
        return Math.max(naiveKnapsack(items, W - items[i].weight, i+1) + items[i].value,
                        naiveKnapsack(items, W, i+1));
    }
    
    // Top down dynamic programming solution. Cache values in a HashMap because 
    // the cache may be sparse so we save space
    public static int topDownKnapsack(Item[] items, int W) {
        // Map: i -> W -> value
        Map<Integer, Map<Integer, Integer>> cache = new HashMap<Integer, Map<Integer, Integer>>();
        return topDownKnapsack(items, W, 0, cache);
    }
    
    // Overloaded recursive function
    private static int topDownKnapsack(Item[] items, int W, int i, Map<Integer, Map<Integer, Integer>> cache) {
        if (i == items.length) return 0;
        
        // Check if the value is in the cache
        if (!cache.containsKey(i)) cache.put(i, new HashMap<Integer, Integer>());
        Integer cached = cache.get(i).get(W);
        if (cached != null) return cached;
        
        // If not, compute the item and add it to the cache
        int toReturn;
        if (W - items[i].weight < 0) {
            toReturn = topDownKnapsack(items, W, i+1, cache);
        } else {
            toReturn = Math.max(topDownKnapsack(items, W - items[i].weight, i+1, cache) + items[i].value,
                                topDownKnapsack(items, W, i+1, cache));
        }
        cache.get(i).put(W, toReturn);
        return toReturn;
    }
    
    // Iterative bottom up solution.
    public static int bottomUpKnapsack(Item[] items, int W) {
        // Initialize cache
        int[][] cache = new int[items.length + 1][W + 1];
        // For each item and weight, compute the max value of the items up to 
        // that item that doesn't go over W weight
        for (int i = 1; i <= items.length; i++) {
            for (int j = 0; j <= W; j++) {
                if (items[i-1].weight > j) cache[i][j] = cache[i-1][j];
                else cache[i][j] = Math.max(cache[i-1][j], cache[i-1][j-items[i-1].weight] + items[i-1].value);
            }
        }
        
        return cache[items.length][W];
    }
    
    // Optimized bottom up solution with 1D cache. Same as before but only save
    // the cache of i-1 and not all values of i.
    public static int bottomUpOptimizedKnapsack(Item[] items, int W) {
        int[] cache = new int[W + 1];
        for (Item i : items) {
            int[] newCache = new int[W + 1];
            for (int j = 0; j <= W; j++) {
                if (i.weight > j) newCache[j] = cache[j];
                else newCache[j] = Math.max(cache[j], cache[j - i.weight] + i.value);
            }
            cache = newCache;
        }
        
        return cache[W];
    }
    
        // Sample testcases
    public static void main(String[] args) {
        (new TestCase(new Item[]{}, 0, 0)).run();
        (new TestCase(new Item[]{
            new Item(4, 5),
            new Item(1, 8),
            new Item(2, 4),
            new Item(3, 0),
            new Item(2, 5),
            new Item(2, 3)
        }, 3, 13)).run();
        (new TestCase(new Item[]{
            new Item(4, 5),
            new Item(1, 8),
            new Item(2, 4),
            new Item(3, 0),
            new Item(2, 5),
            new Item(2, 3)
        }, 8, 20)).run();
        
        System.out.println("Passed all test cases");
    }
    
    // Class for defining and running test cases
    private static class TestCase {
        private Item[] items;
        private int weight;
        private int output;
        
        private TestCase(Item[] items, int weight, int output) {
            this.items = items;
            this.weight = weight;
            this.output = output;
        }
        
        private void run() {
            assert naiveKnapsack(items, weight) == output:
                "naiveKnapsack failed for items = " + itemsString() + ", weight = " + weight;
            assert topDownKnapsack(items, weight) == output:
                "topDownKnapsack failed for items = " + itemsString() + ", weight = " + weight;
            assert bottomUpKnapsack(items, weight) == output:
                "bottomUpKnapsack failed for items = " + itemsString() + ", weight = " + weight;
            assert bottomUpOptimizedKnapsack(items, weight) == output:
                "bottomUpOptimizedKnapsack failed for items = " + itemsString() + ", weight = " + weight;
        }
        
        private String itemsString() {
            StringBuilder sb = new StringBuilder();
            sb.append("[");
            for (int i = 0; i < items.length; i++) {
                Item item = items[i];
                sb.append("{w:" + item.weight + ",v:" + item.value + "}");
                if (i != items.length - 1) sb.append(",");
            }
            sb.append("]");
            
            return sb.toString();
        }
    }
}