def factorial(num):
    res=1
    for i in range(1,num+1):
        res=res*i

    return res

n=int(input('Enter a number'))
print(f"Factorial of {n} id {factorial(n)}")

print('Using recursion ')

def facto(n):
    if n ==0:
        return 1
    else:
        return n*facto(n-1)

print(f"Factorial of {n} evaluated in method 2 is  {facto(n)}")