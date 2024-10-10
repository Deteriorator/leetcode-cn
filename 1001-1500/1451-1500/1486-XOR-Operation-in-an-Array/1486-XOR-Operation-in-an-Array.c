#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0


int xorOperation(int n, int start) {
    int res = 0;
    for (int i = 0; i<n; i++) {
        res ^= start + 2 * i;
    }
    return res;
}
