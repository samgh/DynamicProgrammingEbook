//
//  MakingChange.cpp
//  DynamicProgrammingEbook
//
//  Created by Arjun Singh on 07/29/19.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <stdio.h>
#include <limits.h>

int makeChange(int c){
    int coins[4] = {25,10,5,1}, coins_len = 4;
    int cache[c+1], i, j, minCoins, curCoins;
    cache[0] = 0;

    for(i = 1; i<=c; i++){
        minCoins = INT_MAX;
        for(j = 0; j<coins_len; j++){
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

void test(){
    int i, inputs[3] = {1,6,49}, input_len = 3;
    for(i = 0; i<input_len; i++){
        printf("makeChange(%d): %d\n", inputs[i], makeChange(inputs[i]));
    }
}

int main(){
    test();
    return 0;
}

