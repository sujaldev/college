# Write a program to check if the input string is a palindrome or not.

original = input("Enter a string: ")
print("Given string is", "a" if original == original[::-1] else "not a", "palindrome.")
