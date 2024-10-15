#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

bool isUgly(int n) 
{
    if (n <= 0) 
    {
        return false;
    }
    int factors[] = {2, 3, 5};
    for (int i = 0; i < 3; i++) 
    {
        while (n % factors[i] == 0)
        {
            n /= factors[i];
        }
    }
    return n == 1;
}

