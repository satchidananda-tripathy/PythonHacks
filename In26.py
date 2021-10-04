# Longest substring between two strings

str1='Hello how ate you'
str2="Hello how it's going"

common=[]
for i in range(len(str1)):
    for j in range(len(str2)):
        if (i!=j):
            continue
        elif str1[i] == str2[j] :
            common.append(str1[i])

print(common)

