// Create an array of integer with size n. Return the difference between the largest and the smallest value inside that
// array.
#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = (int) (sizeof(arr) / sizeof(int));

    int min = 0, max = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] < min)
            min = arr[i];
        if (arr[i] > max)
            max = arr[i];
    }

    printf("Minimum = %d; Maximum = %d; Difference = %d", min, max, max-min);

    return 0;
}
