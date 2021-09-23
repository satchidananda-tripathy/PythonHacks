print('Fetch value 30 from below object')
lst=[1,2,{'ack':1,'bar':{'p':10,'q':20,'r':30},4:'abc'},[10,20]]
print(lst)
print("Answer is lst[2]['bar']['r'] : ", end=' ')
print(lst[2]['bar']['r'])

print('---------------')
a={} #By default system assume it is an empty dictionary with no value and no key
b={1}
print(type(a))
print(type(b))
print('-------------------------')
d={(1,2),(3,4),(5,6)}
print(type(d))
print("above one looks like dictionary but it don't contain : , it is a set of tuples")

Phone_book = {"Sachin":123456,"Ramesh":34567,"John":456890,"Lee":23456}
print('---------Method 1----------------')
print ('Iterate the dictionary')

for i in Phone_book:
    print(f" name is {i} phone number is {Phone_book[i]}")


print('-----------Method 2--------------')
print ('Iterate the dictionary')
for name,phone in Phone_book.items():
    print(f" name is {name} phone number is {phone}")