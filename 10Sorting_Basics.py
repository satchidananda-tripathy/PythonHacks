lst=[(1,"Ram",250),
     (2,"Shyam",421),
     (3,"Madhu",233),
     (4,"Jadu",89)]

# Sort the students based on their marks
# Explanation : The key can take a function as input so we passed item[2] which will indirectly do  item[2] for lst in item
# and it will pass each mark as keys to the sort function.

lst.sort(key=lambda item:item[2])
print(lst)

#Sort below dictionary
d={
   "Ram":250,
   "Shyam":421,
   "Madhu":233,
   "Jadu":89
   }
def get_val(di):
     values =[]
     for x in di.values():
          values.append(x)
     return values


sorted_stud = sorted(d.items(),key=lambda x:x[1],reverse=False)
print(sorted_stud)

#For the below
lst =[{
   "Ram":250,
   "Shyam":421,
   "Madhu":233,
   "Jadu":89
   }]
d =lst[0]
print('Then perform above tricks')
print(type(d))