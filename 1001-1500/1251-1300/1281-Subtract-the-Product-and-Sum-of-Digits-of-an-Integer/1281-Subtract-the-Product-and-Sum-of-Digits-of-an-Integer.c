#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

int subtractProductAndSum(int n) 
{
    int m = 1, s = 0;
    while (n > 0)
    {
        int i = n % 10;
        n = n / 10;
        s += i;
        m = m * i;
        /* code */
    }
    return m - s;
}
