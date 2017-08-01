/*
 * Title: Making change
 * Author: Sam Gavis-Hughson
 * Date: 08/01/2017
 * 
 * Given an integer representing a given amount of change, write a function to 
 * compute the total number of coins required to make that amount of change. 
 * 
 * eg. (assuming American coins: 1, 5, 10, and 25 cents)
 * minCoins(1) = 1 (1)
 * minCoins(6) = 2 (5 + 1)
 * minCoins(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)
 * 
 * Execution: javac MakeChange.java && java MakeChange
 */

// We will assume that there is always a 1¢ coin available, so there is always
// a valid way to make the amount of change. We will also implement this as an
// object that is instantiated with a set of coin sizes so we don't have to 
// pass it into our function every time
public class MakingChange {
    private int[] coins;
    
    // Constructor
    public MakingChange(int[] coins) {
        this.coins = coins;
    }
    
    // Greedy algorithm. Take the largest coin possible each time. Doesn't work
    // for all coin systems. We also assume that the coins are in descending 
    // order
    public int greedyMakingChange(int c) {
        int totalCoins = 0; 
        // Remove the largest coin from c that doesn't make c negative
        for (int coin : coins) {
            while (c - coin >= 0) {
                totalCoins++;
                c -= coin;
            }
        }
        return totalCoins;
    }
    
    // Optimized greedy algorithm. By using mods, we can solve this in constant
    // time but this solution has the same limitations
    public int optimalGreedyMakingChange(int c) {
        int totalCoins = 0; 
        // Find how many of each coin can go into the remaining total
        for (int coin : coins) {
            totalCoins += c / coin;
            c %= coin;
        }
        return totalCoins;
    }
    
    // Brute force solution. Go through every possible combination of coins that
    // sum up to c to find the minimum number
    public int naiveMakingChange(int c) {
        if (c == 0) return 0;
        int minCoins = Integer.MAX_VALUE;
        
        // Try removing each coin from the total and see how many more coins
        // are required
        for (int coin : coins) {
            // Skip a coin if it's value is greater than the amount remaining
            if (c - coin >= 0) {
                int currMinCoins = naiveMakingChange(c - coin);
                if (currMinCoins < minCoins) minCoins = currMinCoins;
            }
        }
        
        // Our recursive call removes one coin from the amount, so add it back
        return minCoins + 1;
    }
    
    // Top down dynamic solution. Cache the values as we compute them
    public int topDownMakingChangeOptimized(int c) {
        // Initialize cache with values as -1
        int[] cache = new int[c + 1];
        for (int i = 1; i < c + 1; i++) cache[i] = -1;
        return topDownMakingChangeOptimized(c, cache);
    }
    
    // Overloaded recursive function
    private int topDownMakingChangeOptimized(int c, int[] cache) {
        // Return the value if it's in the cache
        if (cache[c] >= 0) return cache[c];
        
        int minCoins = Integer.MAX_VALUE;
        
        // Try each different coin to see which is best
        for (int coin : coins) {
            if (c - coin >= 0) {
                int currMinCoins = topDownMakingChangeOptimized(c - coin, cache);
                if (currMinCoins < minCoins) minCoins = currMinCoins;
            }
        }
        
        // Save the value into the cache
        cache[c] = minCoins + 1;
        return cache[c];
    }
    
    // Bottom up dynamic programming solution. Iteratively compute number of 
    // coins for larger and larger amounts of change
    public int bottomUpMakingChange(int c) {
        int[] cache = new int[c + 1];
        for (int i = 1; i <= c; i++) {
            int minCoins = Integer.MAX_VALUE;
            
            // Try removing each coin from the total and see which requires
            // the fewest additional coins
            for (int coin : coins) {
                if (i - coin >= 0) {
                    int currCoins = cache[i-coin] + 1;
                    if (currCoins < minCoins) {
                        minCoins = currCoins;
                    }
                }
            }
            cache[i] = minCoins;
        }
        
        return cache[c];
    }
    
    // Sample testcases
    public static void main(String[] args) {
        int[] americanCoins = new int[]{25, 10, 5, 1};
        int[] randomCoins = new int[]{10, 6, 1};
        
        (new TestCase(americanCoins, 1, 1)).run();
        (new TestCase(americanCoins, 6, 2)).run();
        (new TestCase(americanCoins, 47, 5)).run();
        (new TestCase(randomCoins, 1, 1)).run();
        (new TestCase(randomCoins, 8, 3)).run();
        (new TestCase(randomCoins, 11, 2)).run();
        (new TestCase(randomCoins, 12, 2)).run();
        System.out.println("Passed all test cases");
    }
    
    // Class for defining and running test cases
    private static class TestCase {
        private int[] coins;
        private int input;
        private int output;
        
        private TestCase(int[] coins, int input, int output) {
            this.coins = coins;
            this.input = input;
            this.output = output;
        }
        
        private void run() {
            MakingChange mc = new MakingChange(coins);
            assert mc.naiveMakingChange(input) == output:
                "naiveMakingChange failed for input = " + input;
            assert mc.topDownMakingChangeOptimized(input) == output:
                "topDownMakingChangeOptimized failed for input = " + input;
            assert mc.bottomUpMakingChange(input) == output:
                "bottomUpMakingChange failed for input = " + input;
        }
    }
}