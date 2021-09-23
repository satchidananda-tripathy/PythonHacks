#2Sum Int

#Print the numbers where sum of two numbers from this list is equal to target
a = [1,2,3,4,5,6,7,8,9,10]
target = 9

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[i]+a[j]==target:
            print(a[i],a[j])

# If the collection is a set we can not access them by position
print('-------')
a={1,2,3,4,5,6,7,8,9,10}

for i  in a :
    for j in a :
        if i!=j and i+j==target:
            print(i,j)

# METHOD 2
a = [1,2,3,4,5,6,7,8,9,10]
target = 9

print([ (i,j) for i in a for j in a if i!=j and i+j == 9])