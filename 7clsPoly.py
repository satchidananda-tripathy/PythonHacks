#Same name but diff behaviour is called polymorphism

# A human behave different at home and different at office so If office is a class every person in office are objects.

# Method overloading, Method overriding, Ducky Typing and Operator Overloading part of Polymorphism

print('Duck Typing')
print('If a bird walk like a duck, quack like a duck  and looks like a duck then it is a Duck')

print('''Duck typing is a concept related to dynamic typing, 
where the type or the class of an object is less important than the methods it defines. 
When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute''')

class Duck:
    def sound(self):
        print('QUACK QUACK')
class Dog:
    def sound(self):
        print('WOOF WOOF')

class Cat:
    def sound(self):
        print('MEOW MEOW')

def all_sound(x):
    x.sound()

dk = Duck()
print("Duck sounds like ",end=' ')
all_sound(dk)

dg = Dog()
print("Dog sounds like ",end=' ')
all_sound(dg)

ct = Cat()
print("Cat sounds like ",end=' ')
all_sound(ct)

print("Here it doesn't matter which class and method but it only metters whether the class have the given method present or not")