class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    def display_employee(self):
        print("Name:", self.name, "Salary:", self.salary)
empl = Employee("Dave", 10000)
empl.display_employee()

class Freelance(Employee):
    def __init__(self, name, salary, email):
        super.__init__(name, salary)
        self.email = email
    def display_email(self):
        print("Email", self.email)
empl2 = Freelance("dave!@gmail.com")
empl2.display_email()