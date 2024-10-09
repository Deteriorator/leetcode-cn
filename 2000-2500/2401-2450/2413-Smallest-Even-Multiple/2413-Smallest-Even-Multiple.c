#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int smallestEvenMultiple(int n) {
    int m = n % 2;
    if (m == 0) {
        return n;
    } else {
        return n * 2; 
    }
}

int smallestEvenMultiple(int n) {
    return n % 2 == 0 ? n : 2 * n;
}
