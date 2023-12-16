// Write a C program to multiply two matrices.

#include <stdio.h>

void inputMatrix(char name, int arr[][10], int rows, int columns) {
    printf("\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            printf("Enter %c_%d%d: ", name, i + 1, j + 1);
            scanf("%d", &(arr[i][j]));
        }
    }
}

void printMatrix(int arr[][10], int rows, int columns) {
    printf("\n");
    for (int i = 0; i < rows; i++) {
        printf("| ");
        for (int j = 0; j < columns; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("|\n");
    }
}

int main() {
    int m, n, p, A[10][10], B[10][10], AB[10][10], sum;

    // Read number of rows and columns for first matrix
    printf("Enter number of rows for matrix A (<10): ");
    scanf("%d", &m);
    printf("Enter number of columns for matrix A (<10): ");
    scanf("%d", &n);
    printf("\n");

    // Read only the number of columns in the second matrix as the number of rows must be equal to the number of columns
    // in the first matrix
    printf("Enter number of columns for matrix B (<10): ");
    scanf("%d", &p);

    // Read values for both matrices
    inputMatrix('A', A, m, n);
    inputMatrix('B', B, n, p);

    // Calculate matrix multiplication [O(n^3)]
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            sum = 0;
            for (int k = 0; k < n; k++) {
                sum += A[i][k] * B[k][j];
            }
            AB[i][j] = sum;
        }
    }

    // Print matrix multiplication
    printf("\nThe matrix product AB =");
    printMatrix(AB, m, p);

    return 0;
}