



lst=[(1,"Ram",250),
     (2,"Shyam",21),
     (3,"Madhu",233),
     (4,"Jadu",89)]

# Sort the students based on their marks
# Explanation : The key can take a function as input so we passed item[2] which will indirectly do  item[2] for lst in item
# and it will pass each mark as keys to the sort function.

lst1 = sorted(lst,key=lambda item :item[2])

print(lst1)

lst2 = sorted(lst,key=lambda item :item[2],reverse=True)

print(lst2)

#Sort below dictionary
d={
   "Ram":250,
   "Shyam":21,
   "Madhu":233,
   "Jadu":89
   }
'''
How to fetch values from the list 
def get_val(di):
     values =[]
     for x in di.values():
          values.append(x)
     return values
'''
print('--------------')
print('To unerstand the logic look at below output')
for i in d.items():
    print(i)
print('--------------')

print('Scenario 1')
d1=sorted(d,key=lambda item:d[item])
print(d1)
print('Scenario 2')
d2=sorted(d.items(),key=lambda item:item[1])
print(d2)

print('Scenario 3')
d3=sorted(d.values(),key=lambda item:item)
print(d3)

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

print('-----------')
lst=[[1,"Ram",250],
     [2,"Shyam",21],
     [3,"Madhu",233],
     [4,"Jadu",89]]

lst1 = sorted(lst,key=lambda item:item[2])
print(lst1)