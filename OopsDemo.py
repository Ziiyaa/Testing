class Calculator:

    num = 100

    def __int__(self):
        print("Default object created")

    def __init__(self, a, b):
        self.numa = a
        self.numb = b
        print("Parameterized Object created")

    def getData(self):
        print("This is from the method in class")

    def sum(self):
        return self.numa+self.numb + Calculator.num


obj = Calculator(1, 2) # syntax to create objects in python
obj.getData()
print(obj.num)

obj1 = Calculator(4, 8)
obj1.getData()
print(obj1.sum())
