#Replace None value with previous value present in a list

lst=['a','b','c',None,'d','e','f',None,'g']

i=0
for items in lst:
    if i==0 and items is None:
        lst[i]=lst[-1]
    elif items is None:
        lst[i]=lst[i-1]
    else:
        pass

    i=i+1

print(lst)
print('Second Answer')


