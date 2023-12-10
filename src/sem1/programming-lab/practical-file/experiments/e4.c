// Write a C program to perform arithmetic operations using switch case statement.

#include <stdio.h>

int main() {
    int a, b;
    int operation;

    // Read a
    printf("Enter first number: ");
    scanf("%d", &a);

    // Read b
    printf("Enter second number: ");
    scanf("%d", &b);

    // Read operation
    printf("Enter operation add(1), subtract(2), multiply(3), divide(4): ");
    scanf("%d", &operation);

    // Perform the operation input by the user on a and b
    switch (operation) {
        case 1:
            printf("%d + %d = %d", a, b, a + b);
            break;
        case 2:
            printf("%d - %d = %d", a, b, a - b);
            break;
        case 3:
            printf("%d x %d = %d", a, b, a * b);
            break;
        case 4:
            printf("%d / %d = %f", a, b, (float) a / b);
            break;
        default:
            printf("Invalid operation.");
    }

    return 0;
}