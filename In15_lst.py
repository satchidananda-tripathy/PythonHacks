#Can you do the following without using subquery?: {1,None,1,2,None} --> [1,1,1,2,2]
#Ensure you take care of case input[None] which means None object

s = [1,None,1,2,None]
for pos,value in enumerate(s):
    if value == None:
        s[pos] = s[pos-1]
print(s)
