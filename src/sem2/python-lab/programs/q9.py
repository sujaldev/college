# Write a program to compute the GCD of two numbers.

def gcd(a, b):
    if a < b:
        return gcd(a, b - a)
    elif a > b:
        return gcd(a - b, b)
    return a


print(gcd(
    int(input("Enter first number: ")), int(input("Enter second number: "))
))
