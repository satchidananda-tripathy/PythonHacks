#if divisible by 3 then fizz if by 5 then buzz if by both the fizzbuzz if not then print the number
def fizzbuzz(num):
    if num%3==0 and num%5==0:
        value='fizzbuzz'
    elif num%3==0:
        value='fizz'
    elif num%5==0:
        value='buzz'
    else:
        value=num
    return value

val = fizzbuzz(3)
print(f"output for {3}")
print('------')
print(val)

val = fizzbuzz(5)
print(f"output for {5}")
print('------')
print(val)

val = fizzbuzz(30)
print(f"output for {30}")
print('------')
print(val)

val = fizzbuzz(7)
print(f"output for {7}")
print('------')
print(val)

val = fizzbuzz(0)
print(f"output for {0}")
print('------')
print(val)