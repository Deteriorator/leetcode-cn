#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
// #include <stdbool.h>

typedef int bool;
#define true 1
#define false 0


// official 
int** transpose(int** matrix, int matrixSize, int* matrixColSize, int* returnSize, int** returnColumnSizes) 
{
    int m = matrixSize, n = matrixColSize[0];
    int** transposed = malloc(sizeof(int*) * n);
    *returnSize = n;
    *returnColumnSizes = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) 
    {
        transposed[i] = malloc(sizeof(int) * m);
        (*returnColumnSizes)[i] = m;
    }
    for (int i = 0; i < m; i++) 
    {
        for (int j = 0; j < n; j++) 
        {
            transposed[j][i] = matrix[i][j];
        }
    }
    return transposed;
}
