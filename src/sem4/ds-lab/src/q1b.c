// Initializes an array with ten random integers and then prints four lines of output, containing:
// (a) Every element at an even index.
// (b) Every odd element.
// (c) All elements in reverse order.
// (d) Only the first and last element.
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = (int) (sizeof(arr) / sizeof(int));

    printf("Elements at an even index: ");
    for (int i = 0; i < n; i += 2) {
        printf("%d, ", arr[i]);
    }
    printf("\n");

    printf("Odd numbers: ");
    for (int i = 0; i < n; i++) {
        if (arr[i] % 2 != 0)
            printf("%d, ", arr[i]);
    }
    printf("\n");

    printf("Reverse order: ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%d, ", arr[i]);
    }
    printf("\n");

    printf("First: %d; Last: %d;\n", arr[0], arr[n - 1]);

    return 0;
}
