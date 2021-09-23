#How do you delete duplicates in a list

# Using set
my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]

print(set(my_list))

# Without using set
my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]

unique_list=[]

for items in my_list:
    if items not in unique_list:
        unique_list.append(items)
    else:
        pass

print(unique_list)