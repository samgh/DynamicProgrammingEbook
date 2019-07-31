//
//  Fibonacci.c
//  DynamicProgrammingEbook
//
//  Created by Arjun Singh on 07/29/19.
//

#include <stdio.h>

// Naive recursive Fibonacci solution
int naive(int n){
    if(n < 2)
        return n;
    return naive(n-1) + naive(n-2);
}

// Bottom-up dynamic Fibonacci solution
int bottomUp(int n){
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

int topDown1(int n, int cache[]){
    if(cache[n]>=0)
        return cache[n];

    cache[n] = topDown(n-1, cache) + topDown(n-2, cache);
    return cache[n];
}

// Top-down dynamic Fibonacci solution
int topDown(int n){
    if(n < 2)
        return n;
    int cache[n+1], i;
    for(i = 0; i<=n ; i++)
        cache[i] = -1;
    // Fill initial values in cache
    cache[0] = 0;
    cache[1] = 1;
    return topDown1(n, cache);
}


void test(){
    int i;
    printf("Naive Method:\n");
    for (i=-2; i<9; i++) {
      printf("i=%d, naive(i)=%d\n", i, naive(i));
    }
    printf("\nTop-Down Method:\n");
    for (i=-2; i<9; i++) {
      printf("i=%d, topDown(i)=%d\n", i, topDown(i));
    }
    printf("\nBottom-Up Method:\n");
    for (i=-2; i<9; i++) {
      printf("i=%d, bottomUp(i)=%d\n", i, bottomUp(i));
    }
}

int main(){
    test();
    return 0;
}

