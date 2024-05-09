# Write a program to test and check the mathematical functions such as:
# a) ceil()
# b) sqrt()
# c) pow()
# d) factorial()

from math import ceil, sqrt, pow, factorial

num = 3.14

print(
    f"num: {num}\n",
    f"ceil(num): {ceil(num)}",
    f"sqrt(num): {sqrt(num)}",
    f"pow(num, 2): {pow(num, 2)}",
    f"factorial(5): {factorial(5)}",
    sep="\n"
)
