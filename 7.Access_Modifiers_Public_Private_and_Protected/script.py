class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def show_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

emp = Employee("Hurmat", 50000, "123-45-6789")

print("\nOutside class:")
print("Public - Name:", emp.name)

print("Protected - Salary:", emp._salary)

try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN:", e)

print("Access Private with name mangling:", emp._Employee__ssn)
