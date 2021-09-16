##Here *numbers acts as a tuple. so we need to iterate the tuple to get the result.

def mult(*numbers):
    res=1
    for i in numbers:
        res=res*i
    return res

print(mult(10))

print(mult(10,20))

print(mult(1,2,3,4,5,6))

print(mult())