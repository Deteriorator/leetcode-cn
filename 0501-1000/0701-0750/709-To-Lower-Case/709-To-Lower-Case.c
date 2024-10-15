#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

char* toLowerCase(char* s) 
{
    int len = strlen(s);
    for (int i = 0; i < len; i++)
    {
        s[i] = tolower(s[i]);
    }
    return s;
}