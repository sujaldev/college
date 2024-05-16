# Write a program to check if the given number is an Armstrong number or not. Examples of Armstrong number
# are 153, 370, 371 etc.

num = int(str_num := input("Enter a number: "))

power = len(str_num)
print(
    "Given number is",
    "not an" if sum([int(digit) ** power for digit in str_num]) != num else "an",
    "Armstrong number."
)
