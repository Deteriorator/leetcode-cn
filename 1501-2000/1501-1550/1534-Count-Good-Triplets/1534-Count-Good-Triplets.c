#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0



int countGoodTriplets(int* arr, int arrSize, int a, int b, int c)
{
    int i, j, k, res = 0;
    for (i = 0; i < arrSize; ++i)
    {
        for (j = i + 1; j < arrSize; ++j)
        {
            for (k = j + 1; k < arrSize; k++)
            {

                if ((abs(arr[i] - arr[j]) <= a) && 
                    (abs(arr[j] - arr[k]) <= b) &&
                    (abs(arr[i] - arr[k]) <= c))
                {
                    res = res + 1;
                }
            }
        }
    }
    return res;
}