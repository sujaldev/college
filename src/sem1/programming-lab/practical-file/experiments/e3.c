// Write a C program to find the roots of a quadratic equation.

#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, discriminant, root1, root2;

    // Read a
    printf("Enter x^2 coefficient (a): ");
    scanf("%f", &a);

    // Read b
    printf("Enter x coefficient (b): ");
    scanf("%f", &b);

    // Read c
    printf("Enter constant (c): ");
    scanf("%f", &c);

    // Calculate the discriminant for the given equation
    discriminant = (b * b) - (4 * a * c);

    // Calculate roots by using the quadratic formula
    if (discriminant > 0) {
        root1 = (b + sqrt(discriminant) / (-2 * a));
        root2 = (b - sqrt(discriminant) / (-2 * a));

        printf("Two distinct real roots exist:\n%f\n%f", root1, root2);
    } else if (discriminant == 0) {
        root1 = b / (-2 * a);
        printf("One distinct real root exists:\n%f", root1);
    } else {
        printf("No real roots exist.");
    }

    return 0;
}