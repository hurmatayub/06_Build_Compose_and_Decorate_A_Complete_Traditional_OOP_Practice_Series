class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} engine is starting...")

class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine

    def start_car(self):
        print(f"{self.make} car is ready to start.")
        self.engine.start()

engine = Engine("V8")
car = Car("Mustang", engine)

car.start_car()
