//
//  MakingChange.cpp
//  DynamicProgrammingEbook
//
//  Created by Arjun Singh on 07/29/19.
//

#include <stdio.h>
#include <limits.h>

int bruteForce(int c, int coins[], int coins_len){
    if(c == 0)
        return 0;
    int minCoins = INT_MAX, i;
    for(i = 0; i < coins_len; i++){
        if(c - coins[i] >= 0){
            int curCoins = bruteForce(c-coins[i], coins, coins_len);
             if(curCoins < minCoins)
                minCoins = curCoins;
        }
    }
    return (minCoins + 1);
}

int bottomUp(int c, int coins[], int coins_len){
    int cache[c+1], i, j, minCoins, curCoins;
    cache[0] = 0;

    for(i = 1; i <= c; i++){
        minCoins = INT_MAX;
        for(j = 0; j < coins_len; j++){
            if(i - coins[j] >= 0){
                curCoins = cache[i - coins[j]] + 1;
                if(curCoins < minCoins)
                    minCoins = curCoins;
            }
        }
        cache[i] = minCoins;
    }
    return cache[c];
}

int topDown1(int c, int coins[], int coins_len, int cache[]){
    if(cache[c] >= 0)
        return cache[c];
    int minCoins = INT_MAX, i;
    for(i = 0; i < coins_len; i++){
        if(c - coins[i] >= 0){
            int curCoins = topDown1(c-coins[i], coins, coins_len, cache);
            if(curCoins < minCoins)
                minCoins = curCoins;
        }
    }
    cache[c] = minCoins + 1;
    return cache[c];
}

int topDown(int c, int coins[], int coins_len){
    int cache[c+1], i;
    for(i = 1; i <= c; i++)
        cache[i] = -1;
    cache[0] = 0;
    return topDown1(c, coins, coins_len, cache);
}

void test(){
    int i, inputs[3] = {1,6,49}, input_len = 3, coins[4] = {25,10,5,1}, coins_len = 4;
    printf("Brute Force Method:\n");
    for(i = 0; i<input_len; i++){
        printf("bruteForce(%d): %d\n", inputs[i], bruteForce(inputs[i], coins, coins_len));
    }
    printf("\nTop-Down Method:\n");
    for(i = 0; i<input_len; i++){
        printf("topDown(%d): %d\n", inputs[i], topDown(inputs[i], coins, coins_len));
    }
    printf("\nBottom-Up Method:\n");
    for(i = 0; i<input_len; i++){
        printf("bottomUp(%d): %d\n", inputs[i], bottomUp(inputs[i], coins, coins_len));
    }
}

int main(){
    test();
    return 0;
}

