# Guess the output , before checking the result
import sys as sys
# tuple ordered immutable faster than list and take less memory then list ( as immutable it doesn't have to reserve maximum possible memory on datatype
#t=(2,) tuple
#t=(2) integer

t=(2)
print(type(t))
print('---------')
t1=2,
print(type(t1))
print('------------')
lst=[2]
print(f"size of tuple is {sys.getsizeof(t1)} and size of list is {sys.getsizeof(lst)} ")
print('------------')

print(2*(2)) # Confused ?? Think a bit
print(2*(2,)) # When we swap e.g. a,b = b,a this concept work..
print((2,)+(3,4,5))
print('------------')
t2=((0,))
t2=t2+2*(2,)
print(t2)
print('------------')
print('Below will throw error because it can not add a tuple with int')
print((0,)+5)
