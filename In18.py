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

''' Above functions can be elaborately written as 
    temp,temp1=1,1
      for i in range(len(A) -1) 
         temp = temp * A[i]<=A[i+1] -- if acending order or not
         temp1 = temp1 * A[i]>=A[i+1] -- if descending ( if condition doesn't satisfy for any element it will be 0)
  if (temp == 0 or temp1 == 0) 
      then Not monotonic 
   else 
      Monotonic
        all() check if any of the element is 0 .. if yes then return 0 .. that is similar to multiplying them
         '''

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

