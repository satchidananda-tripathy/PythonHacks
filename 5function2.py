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
a=input('Enter a seris of numbers separated by a comma').split()
print(', is the default delimeter of split function')
print(a)
print('-------------')
print('-------------')
delim = input('Enter a delimiter')
a,*b=input('Enter a seris of numbers separated by a delim').split(delim)
print(a)
print(b)
##input 12
a=input('Enter a number')
print('below will throw error because an int can not be added with str')
a=a+10
print(a)