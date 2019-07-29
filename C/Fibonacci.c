//
//  Fibonacci.c
//  DynamicProgrammingEbook
//
//  Created by Arjun Singh on 07/29/19.
//  Copyright © 2018 Solomon Kinard. All rights reserved.
//

#include <stdio.h>

int fib(int n){
    if(n<2)
        return n;
    int t1 = 1, t2 = 0, i;
    for(i = 2; i<n; i++){
        int t0 = t1+t2;
        t2 = t1;
        t1 = t0;
    }
    return t1 + t2;
}

void test(){
    int i;
    for (i=-2; i<9; i++) {
      printf("i=%d, fib(i)=%d\n", i, fib(i));
    }
}

int main(){
    test();
    return 0;
}

