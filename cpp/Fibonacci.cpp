//
//  FIbonacci.cpp
//  DynamicProgrammingEbook
//
//  Created by Solomon Kinard on 11/16/18.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//


#include <iostream>
#include <stdio.h>

namespace Fibonacci {
  int fib(int n) {
    if (n < 2) return n;
    int n1 = 1, n2 = 0;
    for (int i = 2; i < n; i++) {
      int n0 = n1 + n2;
      n2 = n1;
      n1 = n0;
    }
    return n1 + n2;
  }
  
  void test() {
    for (int i=-2; i<9; i++) {
      printf("i=%d, fib(i)=%d\n", i, fib(i));
    }
  }
}
