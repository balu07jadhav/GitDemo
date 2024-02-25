class Student:
    def __init__(self,name):
        print("This is parameterized constructor")
        self.name = name

    def show(self):
        print(self.name)


student=Student("Balu")
student.show()