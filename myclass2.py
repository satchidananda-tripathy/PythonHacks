#Constructor

class myClass2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def substract(self):
        return self.x-self.y


obj1=myClass2(20,15)
obj2=myClass2(4,2)

print(f"The addition of numbers in obj1 are {obj1.add()}")
print(f"The substraction of numbers in obj2 are {obj2.substract()}")