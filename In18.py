'''Given an array of integers, we would like to determine whether the array is monotonic
(non-decreasing/non-increasing) or not. Examples:
 // 1 2 5 5 8
// true
// 9 4 4 2 2
// true
// 1 4 6 3
// false
//1 1 1 1 1 1
// true
'''

def chk_monotonic(A):
    x=all(A[i]<=A[i+1] for i in range(len(A)-1))
    y=all(A[i]>=A[i+1] for i in range(len(A)-1))
    return x or y

X =[1 ,2, 5 ,5 ,8]

if(chk_monotonic(X)):
    print(X,'Is','Monotonic')
else:
    print(X,'Is','Non Monotonic')


X =[1 ,2, 9 ,5 ,8]

if(chk_monotonic(X)):
    print(X,'Is','Monotonic')
else:
    print(X,'Is','Non Monotonic')


X =[1 ,0, -1 ,-2 ,-3]

if(chk_monotonic(X)):
    print(X,'Is','Monotonic')
else:
    print(X,'Is','Non Monotonic')

