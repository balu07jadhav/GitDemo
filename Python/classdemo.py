class Calculator:
    num = 100
    # default constructor

    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("constructor executed")

    def getData(self):
        print("Inside methods")

    def Summation(self):
        return self.firstnumber + self.secondnumber + self.num


obj1=Calculator(2,3) #object created
obj1.getData()
print(obj1.Summation())

obj2=Calculator(1,5) #object created
obj2.getData()
print(obj2.Summation())


