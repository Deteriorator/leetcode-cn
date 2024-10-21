#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0


bool cmpp(char a) 
{
    if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') 
    {
        return true;
    }
    return false;
}

int vowelStrings(char** words, int wordsSize, int left, int right) 
{
    int i, j;
    int len;
    int output = 0;

    for (i = left; i <= right; ++i) 
    {
        len = strlen(words[i]);
        if (cmpp(words[i][0]) && cmpp(words[i][len - 1])) 
        {
            output++;
        }
    }

    return output;
}
