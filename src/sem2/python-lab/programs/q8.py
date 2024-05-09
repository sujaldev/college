# Write a program that receives marks of a student for a subject as input and assigns a grade A||B||C||D||E||F.

# Changing the distribution is as easy as changing the 9 below to lower integers (higher values would mean no A grade).
offset = 9 - int(input("Enter marks for subject (0 - 100): ")) // 10
positive_offset = (abs(offset) + offset) // 2  # Makes negative values equal zero
print(chr(65 + positive_offset) if offset <= 5 else "F")
