# A basic class with a constructor
class Dog:
    @classmethod
    def Ibark(cls):
        print('Woof Woof')

    def __init__(self,name):
        self.name=name
        print('I am a constructor')
        print(f" The object {self.name} got initialized")

    def printNm(self):
        print(f"My name is : {self.name}")


d = Dog('Kubur')
Dog.Ibark()
d.printNm()