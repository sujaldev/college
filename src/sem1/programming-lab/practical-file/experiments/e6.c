// Write a C program to find GCD of two integers by using a recursive function.

#include <stdio.h>

int gcd(int a, int b) {
    if (b != 0) {
        return gcd(b, a % b);
    }
    return a;
}

int main() {
    int a, b;

    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    printf("GCD(%d, %d) = %d", a, b, gcd(a, b));

    return 0;
}