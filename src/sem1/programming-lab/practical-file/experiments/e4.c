// Write a C program to find the factorial of a given integer using non-recursive function.

#include <stdio.h>

int main() {
    // Initialize fact to 1 since 0! = 1
    int fact = 1, n;

    // Read n
    printf("Enter number: ");
    scanf("%d", &n);

    // Keep multiplying fact by the current value of n and subtract 1 from n on each iteration.
    while (n != 0) {
        fact *= n;
        n -= 1;
    }

    // Output factorial
    printf("Factorial is %d", fact);
    return 0;
}