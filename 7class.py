'''
Write a program to create a class Calculator
Define methods addition, substraction, multiplication and division takes two numbers and return the resultant number

define another method called named_execute_command which takes a string 'command' and two numbers as an arguement
the command string can be add, mul, sub, div.

the command should dynamically call the required function.

Note: make the command case insitive
'''

class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self,a,b):
        return a+b
    def substraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def diivsion(self,a,b):
        if b == 0:
            print('Can not divide')
            return 0
        else:
            return a/b
    def named_execute_command(self,cmd):
        if cmd.lower() == 'add':
            print('The addition is ')
            print(self.addition(self.a,self.b))
        elif cmd.lower() == 'sub':
            print('The Substraction is ')
            print(self.substraction(self.a,self.b))
        elif cmd.lower() == 'mul':
            print('The Multiplication is ')
            print(self.multiplication(self.a,self.b))
        if cmd.lower() == 'div':
            print('The Division is ')
            print(self.diivsion(self.a,self.b))

cal = Calculator(5,6)

cal.named_execute_command('add')
cal.named_execute_command('sub')

cal.named_execute_command('mul')

cal.named_execute_command('div')






