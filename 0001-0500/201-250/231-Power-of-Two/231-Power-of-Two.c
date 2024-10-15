#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0


bool isPowerOfTwo(int n) 
{
    return n > 0 && ( n & (n - 1)) == 0;
    //
    // while ( n!=0 && n%2==0)
    // { 
    //     n /= 2; 
    // } 
    // return n==1;
}
