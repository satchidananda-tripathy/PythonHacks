# Enter a number and check if it is prime or not

def is_a_prime(num):
    for x in range(2,num,1):
        if num%x == 0:
            return 0
            break
    else:
        return 1

print('Prime' if is_a_prime(31)==1 else 'Not a prime')