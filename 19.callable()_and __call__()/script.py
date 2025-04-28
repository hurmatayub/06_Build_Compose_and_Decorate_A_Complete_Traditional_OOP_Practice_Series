class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor

multiplier = Multiplier(5)

print(callable(multiplier))

result = multiplier(10)
print(result)
