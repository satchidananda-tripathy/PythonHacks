class Myclass:
    def prnthello(self):
        print('Hello')

obj = Myclass()
obj.prnthello()
print('Check if obj is an object of Myclass class')
print(isinstance(obj,Myclass))