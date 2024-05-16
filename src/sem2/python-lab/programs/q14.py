# Write a program to print a multiplication table of a given number.

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


table(int(input("Enter a number: ")))
