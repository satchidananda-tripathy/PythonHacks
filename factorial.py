def factorial(num):
    res=1
    for i in range(1,num+1):
        res=res*i

    return res

n=int(input('Enter a number'))
print(f"Factorial of {n} id {factorial(n)}")