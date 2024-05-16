# Write a program to compute factorial of a given number.

def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


print(fac(int(input("Enter a number: "))))
