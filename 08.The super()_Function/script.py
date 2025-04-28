class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person Constructor: Name set to {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher Constructor: Subject set to {self.subject}")

t = Teacher("Hurmat", "Python")
