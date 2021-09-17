import numpy as np
a =np.array([[1,2,3],[3,4,1],[5,6,8]],int)

a+=2
print(a)
a*=2
print('Multiplied each elements by 2')
print(a)
a**=2
print('Raised each elements to the power of 2')
print(a)
print('sine of each values')
print(np.sin(a))

print(a)
print('column with max values : ')
print(np.max(a,axis=0))
print('rows with max values : ')
print(np.max(a,axis=1))
print('Biggest element in the array')
print(np.max(a))
