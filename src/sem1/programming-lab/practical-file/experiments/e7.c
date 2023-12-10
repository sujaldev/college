// Write a C program to find the largest and smallest number in a list of integers.

#include <stdio.h>

int main() {
    int size = 5, arr[size];

    // Read array
    for (int i = 0; i < size; i++) {
        // Another approach would be to merge the second loop right here
        printf("Enter number %i: ", i+1);
        scanf("%d", &arr[i]);
    }

    int smallest, largest;
    smallest = largest = arr[0];

    // Find largest and smallest
    for (int j = 0; j < size; j++) {
        if (arr[j] < smallest) {
            smallest = arr[j];
        }

        if (arr[j] > largest) {
            largest = arr[j];
        }
    }

    // Output largest and smallest
    printf("Smallest: %d\nLargest: %d", smallest, largest);

    return 0;
}