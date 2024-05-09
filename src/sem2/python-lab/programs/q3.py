# Write a program that receives a number as input from user and returns if it is odd or even number.

num = int(input("Enter an integer: "))
print(f"{num} is {'even' if num % 2 == 0 else 'odd'}.")
