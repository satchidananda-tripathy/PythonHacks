#write a function to check if a year is leap year or not
'''if year is divisible by 400 then is_leap_year
else if year is divisible by 100 then not_leap_year
else if year is divisible by 4 then is_leap_year
else not_leap_year'''

def leap_year(year):
    if year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    elif year % 4 == 0:
        leap = 1
    else:
        leap = 0
    return leap

print ('Leap' if leap_year(2020) else 'Not leap')

#################################
#Write a function to accept a list as input and return a list contains even numbers from first list

def _evnLst(lst):
    x=[i for i in lst if i%2==0]
    return x

print('Even from a list')
l=[1,2,3,4,5,6,7]
print(_evnLst(l))

##################################
# Write a function to take two arrays as input and return members of first array that present in second array

def _firstInSec(lst1,lst2):
    Tlst=[]
    for fitm in lst1:
        if fitm in lst2:
            Tlst.append(fitm)

    return Tlst
print('Common  from a list1 in list2')
FirstLst=[1,2,3,4]
SecondLst=[3,4,5,6,7]
print(_firstInSec(FirstLst,SecondLst))