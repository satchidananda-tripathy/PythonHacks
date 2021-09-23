lst=[10,20,30,40,50,60,90]

print("every 3rd number")
print(lst[::3])

print("Reverse the list")
print(lst[::-1])

print("every 3rd number in reverse order")
print(lst[::-3])

print('Using list comprehension add 5 to the numbers who are divisible by 20')
##lst1=[expression for items in lst if <cond>]

lst1=[item+5 for item in lst if item%20==0]
print(lst1)

lst1 = [('tv',10000),('iphone',50000),('smartwatch',12000)]

print('price of item extracted as follows ')
#print price of the items
for (name,price) in lst1:
    print(price,end=' ')
print('Here  each items in the loop are tuples so we can unpack using two variable as x,y=value1,value2 ')

#Using comprehension

print('\nFollowing result obtained using comprehension')
price=[y for (x,y) in lst1]
print(price)

#return items with price >10000
lst2=[name for (name,price) in lst1 if price>10000]
print('Below items has cost more than 10K')
print(lst2)

lst3 = [('tv',900000),('iphone',50000),('smartwatch',12000)]

#sort the list as per the price of the items.

print('Here for each elements the lamda function will be executed and the value of item[1] will be returned to key based on which the list will be sorted')
lst3.sort(key=lambda item: item[1],reverse=True )
print(lst3)

empty_lst=[]
if not empty_lst:
    print('Empty list')
else:
    print('List is not empty')





