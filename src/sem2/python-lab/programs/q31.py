# Define Employee Class with fields such as Employee ID and Employee Name. Instantiate the class, invoke the
# constructor and make a call to user defined function to display the information about employee.


class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Name: {self.name}\nID: {self.emp_id}")


Employee("04119051723", "Sujal Singh").display()
