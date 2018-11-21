//
//  SquareSubmatrix.cpp
//  DynamicProgrammingEbook
//
//  Created by Solomon Kinard on 11/16/18.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <iostream>
#include <vector>

using std::vector;
using std::min;

namespace SquareSubmatrix {
  int squareSubmatrix(vector<vector<bool>> &vec) {
    int max = 0;
    int n = (int)vec.size();
    vector<vector<int>> cache(n, vector<int>(n));
    for (int i=0; i<cache.size(); i++) {
      for (int j=0; j<cache[0].size(); j++) {
        if (i==0 || j==0) {
          cache[i][j] = vec[i][j];
        } else if (vec[i][j]) {
          cache[i][j] = min(min(cache[i][j-1],cache[i-1][j]), cache[i-1][j-1]) + 1;
        }
        if (cache[i][j] > max) {
          max = cache[i][j];
        }
      }
    }
    return max;
  }
  
  void test() {
    vector<vector<bool>> grid = {
      {1,1,1,1,1},
      {1,1,1,1,0},
      {1,1,1,1,0},
      {1,1,1,1,0},
      {1,0,0,0,0},
    };
    int output = squareSubmatrix(grid);
    int expected = 4;
    assert(output == expected);
  }
}
