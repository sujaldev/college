# Write a program to create a file called “input.txt”, initialize it with a string of your choice and perform the read
# operation to read only the first 3 characters from the file.

with open("input.txt", "w") as file:
    file.write("Hello, World!")

with open("input.txt") as file:
    print(file.read(3))
