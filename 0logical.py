# Guess the output , before checking the result
print('-------------')
print(bool(0))
print(bool('0'))
print('-------------')
print('Below prints true for both as r and s both are string .. they ar not boolean ')
r='True'
s='False'
print(bool(r),bool(s))
print('Below prints 1 for both as r and s both are string .. they ar not boolean.. after conversion also they are true ')
r=bool('True')
s=bool('False')
print(int(r),int(s))

print('-------------')
lst1=[1,2,3]
print(lst1[::-1])
#Below will rturn none because it will simply reverse the list but won't have any return type
print(lst1.reverse())

lst=[1,2,3,4,5,4,3,2,1]

if lst.reverse()==lst[::-1]:
    print('pelindrome list')
print("above statement won't get executed because lst.reverse() don't return anything")

print('-------------')