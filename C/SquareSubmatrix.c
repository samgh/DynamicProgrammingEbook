//
//  SquareSubmatrix.c
//  DynamicProgrammingEbook
//
//  Created by Arjun Singh on 08/01/19.
//

#include <stdio.h>
#include <stdbool.h>

// General function to find the Minimum of two numbers
int MIN(int a, int b){
    if(a <= b)
        return a;
    return b;
}

// General function to find the Minimum of two numbers
int MAX(int a, int b){
    if(a >= b)
        return a;
    return b;
}

// Recursive function used by bruteForce method
int squareSubmatrixbrute(bool ar[][10], int n, int m, int i, int j){
    if(i == n || j == m || !ar[i][j])
        return 0;

    return 1 + MIN(
               MIN(squareSubmatrixbrute(ar, n, m, i+1, j),
                   squareSubmatrixbrute(ar, n, m, i, j+1)),
                   squareSubmatrixbrute(ar, n, m, i+1, j+1));
}

// Brute force solution, uses squareSubmatrixbrute as a recursive subroutine
int bruteForce(bool ar[][10], int n, int m){
    int max = 0, i, j;
    for(i = 0; i < n; i++){
        for(j = 0; j < m; j++){
            if(ar[i][j]){
                max = MAX(max, squareSubmatrixbrute(ar, n, m, i, j));
            }
        }
    }
    return max;
}

// Recursive function used by topDown method
int squareSubmatrixtopDown(bool ar[][10], int n, int m, int i, int j, int cache[][10]){
    if(i == n || j == m || !ar[i][j])
        return 0;
    if(cache[i][j]>0)
        return cache[i][j];
    cache[i][j] = 1 + MIN(
                    MIN(squareSubmatrixtopDown(ar, n, m, i+1, j, cache),
                        squareSubmatrixtopDown(ar, n, m, i, j+1, cache)),
                        squareSubmatrixtopDown(ar, n, m, i+1, j+1, cache));
    return cache[i][j];
}

// Top-down dynamic programming solution, uses squareSubmatrixtopDown as a recursive subroutine
int topDown(bool ar[][10], int n, int m){
    int cache[10][10], i, j;
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            cache[i][j] = 0;
    int max = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < m; j++){
            if(ar[i][j]){
                max = MAX(max, squareSubmatrixtopDown(ar, n, m, i, j, cache));
            }
        }
    }
    return max;
}

// Bottom-up dynamic programming solution, makes no recursive calls.
int bottomUp(bool ar[][10], int n, int m){
    int max = 0, cache[10][10], i, j;
    for(i = 0; i < n; i++)
        for(j = 0; j < m; j++)
            cache[i][j] = 0;
    for(i = 0; i < n; i++){
        for(j = 0; j < m; j++){
            if(i == 0 || j == 0)
                cache[i][j] = (ar[i][j]) ? 1 : 0;
            else if(ar[i][j]){
                cache[i][j] = 1 + MIN(
                                  MIN(cache[i-1][j],
                                      cache[i][j-1]),
                                      cache[i-1][j-1]);
            }
            if(cache[i][j]>max)
                max = cache[i][j];
        }
    }
    return max;
}

void test(){
    bool input1[][10] = {{true, true, true, false},
                        {true, true, true, true},
                        {true, true, true, false}};
    bool input2[][10] = {{true, true, true, true, true},
                         {true, true, true, true, false},
                         {true, true, true, true, false},
                         {true, true, true, true, false},
                         {true, false, false, false, false}};
    bool input3[][10] = {{true, true, false, false, false},
                         {true, true, false, false, false},
                         {false, false, true, true, true},
                         {false, false, true, true, true},
                         {false, false, true, true, true}};
    int i, j;
    printf("Test 1:\n");
    for(i = 0; i<3; i++){
        for(j = 0; j<4; j++){
            if(input1[i][j] == true)
                printf("T ");
            else
                printf("F ");
        }
        printf("\n");
    }
    printf("BruteForce(Test 1): %d\n", bruteForce(input1, 3, 4));
    printf("TopDown(Test 1): %d\n", topDown(input1, 3, 4));
    printf("BottomUp(Test 1): %d\n", bottomUp(input1, 3 ,4));

    printf("\nTest 2:\n");
    for(i = 0; i<5; i++){
        for(j = 0; j<5; j++){
            if(input2[i][j] == true)
                printf("T ");
            else
                printf("F ");
        }
        printf("\n");
    }
    printf("BruteForce(Test 2): %d\n", bruteForce(input2, 5, 5));
    printf("TopDown(Test 2): %d\n", topDown(input2, 5, 5));
    printf("BottomUp(Test 2): %d\n", bottomUp(input2, 5 ,5));

    printf("\nTest 3:\n");
    for(i = 0; i<5; i++){
        for(j = 0; j<5; j++){
            if(input3[i][j] == true)
                printf("T ");
            else
                printf("F ");
        }
        printf("\n");
    }
    printf("BruteForce(Test 3): %d\n", bruteForce(input3, 5, 5));
    printf("TopDown(Test 3): %d\n", topDown(input3, 5, 5));
    printf("BottomUp(Test 3): %d\n", bottomUp(input3, 5 ,5));


}

int main(){
    test();
    return 0;
}


