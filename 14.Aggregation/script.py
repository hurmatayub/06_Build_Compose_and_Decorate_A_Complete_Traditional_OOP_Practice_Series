class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            employee.display()

emp1 = Employee("John", "Manager")
emp2 = Employee("Jane", "Developer")

dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
