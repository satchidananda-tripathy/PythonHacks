g = (i for i in range(10))

print(g)
print('Generator takes less memory than list or tuple because it generate new value in each iteration as per the defination')
print('When we need to deal with huge list of data we should use generator')
for x in g:
    print(x)

print('As generator generate values in each iteration , we can not find len() of generator')

# Unpacking Operator.

print('By putting an * before an iterator we can unpack the values :')
print('Example:')
lst = [1,2,3]
str = "Hello"
t = (1,2,3,4)

print('value of list is : ',end =' ')
print(lst)
print('value of string is :', end =' ')
print(str)
print('value of tuple is : ',end =' ')
print(t)

print('After unpacking list is  =',end =' ')
print(*lst)
print('After unpacking string is  =',end =' ')
print(*str)
print('After unpacking tuple is  =',end =' ')
print(*t)
print('---------------------------')
print('To unpack dictionary we need to put **')
d1={1:'a',2:'b',3:'c'}
d2={1:'a',2:'b',3:'c1',4:'d'}
d = {**d1,**d2}
print(d)