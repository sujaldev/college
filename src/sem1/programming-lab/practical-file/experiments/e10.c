// Write a C program to check whether a matrix is symmetric or not.

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
    int size, matrix[10][10];

    // Read number of rows and columns
    printf("Enter size of square matrix (<10): ");
    scanf("%d", &size);

    // Read values for both matrices
    inputMatrix('a', matrix, size, size);

    // Check symmetricality
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++) {
            if (matrix[i][j] != matrix[j][i]) {
                // Asymmetric elements found, abort.
                printf("\nThe given given matrix, A =");
                printMatrix(matrix, size, size);
                printf("is not symmetric as a_%d%d does not equal a_%d%d", i + 1, j + 1, j + 1, i + 1);
                return 0;
            }
        }
    }

    // This step will only be reached if no asymmetric elements are found while iterating over the matrix.
    printf("\nThe given given matrix, A =");
    printMatrix(matrix, size, size);
    printf("is symmetric.");
    return 0;
}