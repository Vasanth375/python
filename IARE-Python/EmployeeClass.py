class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print("Manager's name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Executive(Manager):
    def display_info(self):
        print("Executive:")
        super().display_info()


exe = Executive("Vasanth",2000, "CSE")
exe.display_info()