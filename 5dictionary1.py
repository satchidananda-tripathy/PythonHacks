print('Fetch value 30 from below object')
lst=[1,2,{'ack':1,'bar':{'p':10,'q':20,'r':30},4:'abc'},[10,20]]
print(lst)
print("Answer is lst[2]['bar']['r'] : ", end=' ')
print(lst[2]['bar']['r'])

print('---------------')
a={} #By default system assume it is a empty dictionary with no value and no key
b={1}
print(type(a))
print(type(b))
print('-------------------------')
d={(1,2),(3,4),(5,6)}
print(type(d))
print("above one looks like dictionary but it don't contain : , it is a set of tuples")