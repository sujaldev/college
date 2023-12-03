// Write a C program to find the factorial of a given integer using recursive function.

#include <stdio.h>

int factorial(int n) {
    if (n == 0) {
        return 1;
    }

    return n * factorial(n - 1);
}

int main() {
    int n;

    printf("Enter number: ");
    scanf("%d", &n);

    printf("Factorial of %d is %d", n, factorial(n));

    return 0;
}
