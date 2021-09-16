#Enter two numbers and print all prime numbers between them

def is_a_prime(num):
    for x in range(2,num,1):
        if num%x == 0:
            return 0
            break
    else:
        return 1

num1,num2=int(input('Enter first Number: ')),int(input('Enter second Number: '))



## If num1 > num2 consider swapping their values first

if num1 > num2:
    num1,num2 =num2,num1

print(f"Prime numbers between {num1} to {num2}")
print('Processing ..........')

for nums in range(num1,num2+1,1):
    if is_a_prime(nums):
        print(nums,end=', ')
