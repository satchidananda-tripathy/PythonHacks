
#Given a dictionary, print the key for nth highest value present in the dict.
#If there are more than 1 record present for nth highest value then sort the key and print the first one,
d={1:20,12:34,3:2,5:45,4:56,9:91,10:67,11:59}

# Sort the dictionary by key values

---

vals=[]
for x in d.values():
    vals.append(x)

vals.sort(reverse=True)

n = int(input('Enter the nth digit for which you want highest value'))

for i in range(len(vals)):
    if i == n-1:
        max = vals[i]
        print(f"The {n} th Highest Number is {max} ")
        break
else:
    print('Check the input value')

 pending logic to fetch the index