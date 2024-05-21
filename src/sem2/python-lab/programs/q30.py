# Write a program to create a class called "Student" with fields such as: Enrollment Number, USS Name, Branch Name,
# Student Name, etc. Instantiate a class and make a call to user defined function to display the details of students.

class Student:
    def __init__(self, enrollment_number, uss, branch, name):
        self.enrollment_number = enrollment_number
        self.uss = uss
        self.branch = branch
        self.name = name

    def display(self):
        print(
            f"Name: {self.name}",
            f"Enrollment Number: {self.enrollment_number}",
            f"Branch: {self.branch}",
            f"USS: {self.uss}",
            sep="\n"
        )


Student("04119051723", "USAR", "IIOT", "Sujal Singh").display()
