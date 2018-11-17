//
//  TargetSum.cpp
//  DynamicProgrammingEbook
//
//  Created by Solomon Kinard on 11/16/18.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <iostream>
#include <vector>

using std::vector;

namespace TargetSum {
  int targetSum(vector<int> nums, int t) {
    int sum = 0;
    for (int num : nums) sum += num;
    vector<vector<int>> cache(nums.size()+1, vector<int>(2*sum+1));
    if (sum == 0) return 0;
    cache[0][sum] = 1;
    for (int i=1; i<=nums.size(); i++) {
      for (int j=0; j<2*sum+1; j++) {
        int prev = cache[i-1][j];
        if (prev != 0) {
          cache[i][j-nums[i-1]] += prev;
          cache[i][j+nums[i-1]] += prev;
        }
      }
    }
    return cache[nums.size()][sum+t];
  }
  
  void test() {
    vector<int> nums{1,1,1,1,1};
    int t = 3;
    int expected = 5;
    int output = targetSum(nums, t);
    assert(output == expected);
  }
}
