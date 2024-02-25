class Calculation1:
    def Summation(self, a, b):
        return a+b
class Calculation2:
    def Multiplication(self, a, b):
        return a*b
class Derived(Calculation1,Calculation2):
    def Divide(self, a, b):
        return a/b


d = Derived()
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation1, Calculation2))
print(d.Divide(10, 2))
print(d.Multiplication(10, 2))
