//
//  Knapsack.cpp
//  DynamicProgrammingEbook
//
//  Created by Solomon Kinard on 11/16/18.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <iostream>
#include <vector>
#include <tuple>

using std::vector;
using std::tuple;

namespace Knapsack {
  class Item {
  public:
    int weight;
    int value;
    Item(int w, int v): weight(w), value(v) {}
  };
  
  int knapsack(vector<Item> items, int w, int i) {
    if (i == items.size()) return 0;
    if (w - items[i].weight < 0) return knapsack(items, w, i+1);
    return std::max(
                    knapsack(items, w - items[i].weight, i+1) + items[i].value, knapsack(items, w, i+1)
    );
  }
  
  int knapsack(vector<Item> &items, int w) {
    return knapsack(items, w, 0);
  }
  
  void test() {
    vector<Item> items{
      {2,6},
      {2,10},
      {3,12},
    };
    int max_weight = 5;
    int expected = 22;
    int output = knapsack(items, max_weight);
    assert(expected == output);
  }
}
