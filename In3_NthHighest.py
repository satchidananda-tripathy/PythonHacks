##Given a ´dictionary, print the key for nth highest value present in the dict.
# If there are more than 1 record present for nth highest value then sort the key and print the first one.
d = {1:21,2:34,3:9,4:51,5:11,6:35,7:35,8:11,9:9}

lst=[]

#Fetch values from teh dictionary into a list
val = [d[y] for y in d ]

#sort the dictionary
val.sort(reverse=True)
#print the key
k = [y for y in d if d[y]==val[0] ]
print(k)
print('------------------------------------')
print('Method2')
d = {1:21,2:34,3:9,4:51,5:11,6:35,7:35,8:11,9:9}
vals=list()

for k,v in d.items():
    vals.append(v)

max_key=[k for k,v in d.items() if v==max(vals)]

print(max_key)