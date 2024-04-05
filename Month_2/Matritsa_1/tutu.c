#include <stdio.h>

void swapHalves(int matrix[100][100], int m, int n) {
    int i, j, temp;
    
    // Swapping upper and lower halves
    for (i = 0; i < m / 2; i++) {
        for (j = 0; j < n; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[m - 1 - i][j];
            matrix[m - 1 - i][j] = temp;
        }
    }
}

void printMatrix(int matrix[100][100], int m, int n) {
    int i, j;
    
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int m, n, i, j;
    
    printf("Enter the number of rows (m): ");
    scanf("%d", &m);
    
    printf("Enter the number of columns (n): ");
    scanf("%d", &n);
    
    int matrix[m][n];
    
    printf("Enter the elements of the matrix:\n");
    for (i = 0; i < m; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    printf("Original Matrix:\n");
    printMatrix(matrix, m, n);
    
    swapHalves(matrix, m, n);
    
    printf("Matrix after swapping halves:\n");
    printMatrix(matrix, m, n);
    
    return 0;
}