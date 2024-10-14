#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

int addDigits(int num) 
{
    while (num >= 10)
    {
        int sum = 0;
        while (num > 0)
        {
            /* code */
            sum += num % 10;
            num = num / 10;
        }
        num = sum;
    }
    return num;
}


// official
int addDigits(int num){
    return (num - 1) % 9 + 1;
}
