import numpy as np
# This module helps us to creates super fast and memory efficients arrays
#We can store data in 1d, 2d, 3d array etc.
# As numpy has a datatype and it keeps less memory (because of contigous allocation) it needs less time to read data hence it is faster

# x = [1,2] y=[3,4] here the list x*y will throw error
# In numpy we can get resulet [ 3, 8]

a=np.array(([1,2,3]),dtype=int)
b=np.array(([1,2],[3,4],[5,6]),dtype=int)

print('Type of the array b is ',type(b))
print('size of the array b is ',b.shape)
print('The dimension of the array a and b respectively are ',a.ndim ,'and ',b.ndim)
print('The second row and second column value of the array b is ',b[1,1], 'or ', b[1][1])
print('The type of values within the array  and the size are ',b.dtype,'and ',b.size)
print('---------------------------------------------------')

# Matrix initialization
print()
print('Matrix initialization')
z=np.zeros((2,3),dtype=int)
o=np.ones((2,3),dtype=int) # intialize an arry with all values 1
fives=np.full((3,3),5,dtype=int) ##Fill the array with values 5
identity = np.identity((5),dtype=int)

print(z)
print(o)
print(fives)
print('Identity matrix is ',identity)
# create a matrix with random values
r = np.random.random((2,3))
print(r)


#Conditional statements
print(r>0.25)

print(r[r>0.25]) ## A simple way to filter data from a list (logically the true value of r>0.25 )

print('Few Mathematical Functions')
print(np.sum(r))
print(np.average(r))
print(np.max(r))
print(np.floor(r))
print(np.round(r))

print('Few Mathematical Operations')
distance_mit = np.array([100,2000,3456,7689,1234])
distance_km =distance_mit/1000

print(distance_km)

