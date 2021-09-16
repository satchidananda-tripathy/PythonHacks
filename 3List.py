

print('---------------')
x=[[]]*2
print(x)
x.append(1)
print(x)
print(x[0])
print('-----------------------')
print('VERY IMP')
x[0].append(2)
print(x)
print("here 2 appended in both [] [] because when we multiplied 2 , both of these are referring to same memory.. ")
print('-----------------------')
print('Check below example for diff')
y=[[]]
y.append([])
print(y)
y[0].append(1)
print(y)
print('-----------------------')
x=[[2]]*2
print(x)
x[0].append(1)
print(x)
print("here 1 appended in both [2] [2] because when we multiplied 2 , both of these are referring to same memory.. ")


