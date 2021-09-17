# Build a matrix as follows

#1 1 1 1 1
#1 1 0 0 1
#1 0 9 0 1
#1 0 0 1 1
#1 0 0 0 1
import numpy as np
ar = np.ones((5,5),int)
print(ar)
mid=np.zeros((3,3),int)
mid[1,1]=9
print(mid)
ar[1:4,1:4] = mid

print('Final Array is ')
print(ar)