#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0


int numIdenticalPairs(int* nums, int numsSize) {
    int res = 0;
    for (int j = 0; j < numsSize; j++) {
        for (int i = 0; i < j; i++) {
            if (nums[i] == nums[j]) {
                res += 1;
            }
        }
    }
    return res;
}
