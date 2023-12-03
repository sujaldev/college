// Write a C program to find the sum of individual digits using while.

#include <stdio.h>

int main() {
    int num, rem, sum = 0;

    // Read num
    printf("Enter a number: ");
    scanf("%d", &num);

    // Keep removing the one's place from num and add the removed digit to the running sum.
    while (num != 0) {
        rem = num % 10;
        sum += rem;
        num /= 10;
    }

    // Output sum of digits
    printf("Sum of digits = %d", sum);
    return 0;
}
