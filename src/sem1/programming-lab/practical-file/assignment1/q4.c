// Write a C program to find the factorial of a given integer using non-recursive function.

#include <stdio.h>

int main() {
    int fact = 1, n;

    printf("Enter number: ");
    scanf("%d", &n);

    while (n != 0) {
        fact *= n;
        n -= 1;
    }

    printf("Factorial is %d", fact);
    return 0;
}