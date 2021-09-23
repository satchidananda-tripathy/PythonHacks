tup1=(10,20,30)
tup2=(40,50,60)

t_combine=tup1+tup2
print(t_combine)

#access by index
print(t_combine[2])

print(t_combine[-1])

print('multiple by 3 ')
print(t_combine*3)

print(10<<1) #bit wise operator
print(~13) # output is -14  .. find the 2's complement of 13 and check
print(4|6) # bitwise or

x=range(10)
print(sum(x))
print('we can not print x as it is an iterable')
for i in x:
    print(i,end=', ')