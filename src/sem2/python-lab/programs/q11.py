# Write a program to check if the input year is a leap year or not

from calendar import isleap

print(
    "Given year is",
    "a" if isleap(int(input("Enter a year: "))) else "not a",
    "leap year."
)
