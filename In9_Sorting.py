# Sort a list and print , Use predefined function
#list.sort(key=None, reverse =False) Default property of sort function.

#Bubble Sort

#compaire first to second if second is grater than first then swap... now second with third.. third with fourth so on.
# After first iteration the biggest number or smallest will be at last..
# Next loop will go from first number to n-1th number .. and so on.. untill all the list is sorted.

lst =[10,2,34,5,67,87,45,32,1,100]

for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)

#Selection Sort
  #  Concept is same .. but don't swap.. just retain the position and swap at the end of each iteration

lst =[10,2,34,5,67,87,45,32,1,100]

for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]<lst[j+1]:
            pos = j+1
    lst[pos],lst[i]=lst[i],lst[pos]

print(lst)