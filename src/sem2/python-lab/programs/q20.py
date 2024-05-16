# Write a program to create a file called “input.txt”, perform write/read operation on it with a string
# “Computer Science”.

with open("input.txt", "w") as file:
    file.write("Computer Science")

with open("input.txt") as file:
    print(file.read())
