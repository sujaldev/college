// Write a C program to find the factorial of a given integer using recursive function.

#include <stdio.h>

// Recursive implementation of the factorial function,
// similar to how it's mathematically stated in terms of itself.
int factorial(int n) {
    if (n == 0) {
        return 1;
    }

    return n * factorial(n - 1);
}

int main() {
    int n;

    // Read n
    printf("Enter number: ");
    scanf("%d", &n);

    // Output factorial
    printf("Factorial of %d is %d", n, factorial(n));

    return 0;
}
