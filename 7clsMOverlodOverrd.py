#mehod oveloading

class Overload:
    def add(self,*args):
        sum = 0
        for i in args:
            sum = sum+i
        return sum

class Override(Overload):
    def add(self,a,b):
        return str(a)+str(b)

print('Example of Method Overloading ')
print('As per the number of arguments it decideds which function to use')
obj1 = Overload()
print(obj1.add(2,3))
print(obj1.add(1,2,3,4))


obj2 =Override()
print('Although a class inherited from others, if it find a function within it self it override the method of parent class')
print(obj2.add(2,3))