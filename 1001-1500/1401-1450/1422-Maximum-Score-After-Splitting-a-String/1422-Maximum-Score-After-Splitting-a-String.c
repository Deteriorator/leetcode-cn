#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maxScore(char * s)
{
    int ans = 0;
    int n = strlen(s);
    for (int i = 1; i < n; i++) 
    {
        int score = 0;
        for (int j = 0; j < i; j++) 
        {
            if (s[j] == '0') 
            {
                score++;
            }
        }
        for (int j = i; j < n; j++) 
        {
            if (s[j] == '1') 
            {
                score++;
            }
        }
        ans = MAX(ans, score);
    }
    return ans;
}

