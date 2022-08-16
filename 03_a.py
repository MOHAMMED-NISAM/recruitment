class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


class Usecalculation(Calculator):
    def div(self, a, b):
        return a / b


obj1 = Usecalculation()
print(obj1.add(6, 3))
print(obj1.sub(6, 3))
print(obj1.mul(6, 3))
print(obj1.div(6, 3))
