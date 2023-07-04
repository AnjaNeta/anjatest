# class Employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary = salary
#     def display_employee(self):
#         print("Name:", self.name, "Salary:", self.salary)
# empl = Employee("Dave", 10000)
# empl.display_employee()
#
# class Freelance(Employee):
#     def  __init__(self, name, salary, email):
#         super().__init__(name, salary)
#         self.email = email
#     def display_email(self):
#         print("Email", self.email)
# empl2 = Freelance("Dave", 10000, "dave!@gmail.com")
# empl2.display_email()


class Animal:
    def __init__(self, legs, tail, domestic, mammals):
        self.legs = 4
        self.tail = True
        self.domestic = True
        self.mammals = True
    def is_mammals(self):
        if self.mammals:
            print("it s mammal")
    def is_domestic(self):
        if self.domestic:
            print("yep, it's domestic animal")

class Horse(Animal):
    def __init__(self):
        super().__init__()
    def is_legs_and_tail(self):
        super().is_legs_and_tail()
        if legs == 4 and tail = True
hr = Horse()
hr.is_legs_and_tail()

