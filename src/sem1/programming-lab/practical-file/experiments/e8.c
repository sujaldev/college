// Write a C program to sort an array in ascending order.

#include <stdio.h>

int main() {
    int size = 5, arr[size], temp;

    // Read array
    for (int i = 0; i < size; i++) {
        printf("Enter number %i: ", i+1);
        scanf("%d", &arr[i]);
    }

    // Sort the array with bubble sort
    for (int i = 0; i < (size - 1); i++) {
        // Since the last element after each iteration completed in the first loop ensures the greatest number bubbles
        // up to the highest index the second loop need not traverse the whole array.
        for (int j = 0; j < (size - i - 1); j++) {
            // Swap the current and the next number if they're out of order.
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    // Output the sorted array
    printf("[");
    for (int k = 0; k < (size - 1); k++) {
        printf(" '%d' ", arr[k]);
    }
    if (size > 0) {
        printf(" '%d' ", arr[size-1]);
    }
    printf("]");

    return 0;
}