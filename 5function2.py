## Assume
a=input('Enter a number')
print(type(a))
print('-------------')
#


#enter an expression like 5+4
x=input('Enter an expression e.g. 5+4 : ')
print(x)

print('-------------')
#enter an expression like 5+4
y=eval(input('Enter an expression e.g. 5+4 : '))
print(y)

print('-------------')
a=input('Enter a seris of numbers separated by a delim').split()
print(a)
print('-------------')
print('-------------')
a,*b=input('Enter a seris of numbers separated by a delim').split()
print(a)
print(b)
##input 12
a=input('Enter a number')
a=a+10
print(a)