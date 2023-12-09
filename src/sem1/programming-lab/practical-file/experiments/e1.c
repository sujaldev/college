// Write a C program to find the greatest number among three numbers provided by the user using if else.

#include <stdio.h>

int main() {
    int a, b, c, largest;

    // Read first number
    printf("Enter first number: ");
    scanf("%d", &a);

    // Read second number
    printf("Enter second number: ");
    scanf("%d", &b);

    // Read third number
    printf("Enter third number: ");
    scanf("%d", &c);

    if (a >= b && a >= c) {
        // a is larger than both b and c
        // (it might also be equal to one of them or even both)
        largest = a;
    } else if (b >= a && b >= c) {
        // b is larger than both a and c
        // (it might also be equal to one of them or even both)
        largest = b;
    } else {
        // Since a and b aren't the largest, c must be.
        largest = c;
    }

    // Output the largest number among the three.
    printf("%d is the largest number.", largest);
    return 0;
}