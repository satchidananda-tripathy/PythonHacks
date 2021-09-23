#Replace None value with previous value present in a list
# Method 1 to keep last value of arry if first value is None
# Method 2 to skip the computation if first value is None

lst=[None,'a','b','c',None,'d','e','f',None,'g']

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
print('Method 2')


lst=[None,'a','b','c',None,'d','e','f',None,'g']

positions =[pos for pos,val in enumerate(lst) if val==None]
print('None present in the positions' , positions)

for i in positions:
    if i == 0:
        pass
    else:
        lst[i]=lst[i-1]
print(lst)