# print fibonacii numbers untill n
# Using recursion
def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibo(n-1)+fibo(n-2)

num=int(input('How many fibonacci numbers you want to print ? Enter in numeric '))

for i in range(1,num+1):
    print(f"No {i} is : {fibo(i)}")
print('---------------------------------------------------------------')
print('Below is the output of the program done without using recursion')

i,j,next =1,1,1
for items in range(num):
        print(i, end=',')
        next = i+j
        i=j
        j=next

print('----------- Enter a number and print the fibonacii series untill that number')
print('---------------------------------------------------------------')
i,j,k=1,1,0
print(i,j)
n=int(input('enter a number to print fibo series within it'))
while k<n:
    k = i+j
    print(k)
    temp = j
    i = temp
    j = k

