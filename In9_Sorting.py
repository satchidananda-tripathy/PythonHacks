# Sort a list and print , Use predefined function
#list.sort(key=None, reverse =False) Default property of sort function.

#Bubble Sort

lst =[10,2,34,5,67,87,45,32,1,0]

for j in range(len(lst)-1,0,-1):
    #Repeate below steps untill all elements are completed
    for i in range(j):
        # First iteration from 0 to 10th element then the end element will have the biggest one.
        # Second iteration from 0 to 9th element then the end-1 th element will have the biggest one. so on
        # Compaire a value with it's next value if the value is small then swap. Do untill last element.
        if lst[i]>lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
print(lst)

#Selection Sort

lst =[10,2,34,5,67,87,45,32,1,0]

print cd


print(lst)
