//
//  MakingChange.cpp
//  DynamicProgrammingEbook
//
//  Created by Solomon Kinard on 11/16/18.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <stdio.h>
#include <vector>

using std::vector;

namespace MakingChange {
  vector<int> coins{25,10,5,1};
  
  int makeChange(int c) {
    vector<int> cache(c+1);
    for (int i=1; i<=c; i++) {
      int minCoins = INT_MAX;
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
  
  void test() {
    vector<int> inputs{1,6,49};
    for (int input : inputs) {
      printf("makeChange(%d): %d\n", input, makeChange(input));
    }
  }
}
