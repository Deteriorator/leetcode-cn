#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

bool isPowerOfThree(int n) 
{
    while ( n && n % 3 == 0)
    {
        /* code */
        n /= 3;
    }
    return n == 1;
}


