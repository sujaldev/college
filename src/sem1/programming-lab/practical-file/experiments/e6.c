// Write a C program to find GCD of two integers by using a recursive function.

#include <stdio.h>

// Recursive function that calculates the greatest common denominator for 2 positive integers.
int gcd(int a, int b) {
    if (b != 0) {
        return gcd(b, a % b);
    }
    return a;
}

int main() {
    int a, b;

    // Read a
    printf("Enter first number: ");
    scanf("%d", &a);

    // Read b
    printf("Enter second number: ");
    scanf("%d", &b);

    // Output the greatest common denominator of a and b
    printf("GCD(%d, %d) = %d", a, b, gcd(a, b));

    return 0;
}