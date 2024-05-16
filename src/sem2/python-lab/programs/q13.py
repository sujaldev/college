# Write a Program to generate Fibonacci series till 100.

a, b = 0, 1
print(a, end=" ")
while b <= 100:
    print(b, end=" ")
    a, b = b, b + a
