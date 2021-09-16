# Operator overloading
# Write a program to add values of variables within a object and return .. implement like obj = obj1+obj2


class Additions:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        a = self.a+other.a
        num = Additions(a)
        return num

num1 = Additions(20)
num2 = Additions(30)
num3 = num1 + num2 ## This is not possible so we need to overload the existing inbuilt __add__() magic method

print(num3.a)
