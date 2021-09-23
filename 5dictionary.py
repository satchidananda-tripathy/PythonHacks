#Dictionary is mutable with a key value pair, where the key can be formed from an immmutable object.
# key have to be immutable or hashable
# a dictionary can contain another dict or list
D={1:'RAM',2:'SHYAM',3:'MADHU'}

print('Below output doesn\'t give value because we have not used values function, it will assign the keys into the variable value')
for value in D:
    print(value,end=' ')
print()
print('In the above statement if we print D[value] it will give values Or ')
print('Below will print values')
for val in D.values():
    print(val,end=' ')

print('To print keys there is another method')
for k in D.keys():
    print(k,end=' ')

print('------other way to iterate------')

for k,v in D.items():
    print(f"key is {k} value is {v}")

print('=====================================')
print('IMPORTANT')
Y={'a':'abc','d':'def','g':'ghi','j':'jkl'}
if 'a' in Y:
    print('a is present as a Key')

if 'abc' in Y.values():
    print('abc present as values')
print('=====================================')

D1={1:'RAM',2:'SHYAM',3:'MADHU'}
D2=D1
print(D2)
print('----Above will not create copy of dictionary but it will refer to same memory---')
print('Below will create copy')
print(dict(D1.items()))
D3=dict(D1)
print(D3)
D4={}
D4.update(D1)
print(D4)


