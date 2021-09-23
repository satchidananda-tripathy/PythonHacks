
#Given a dictionary, print the key for nth highest value present in the dict.
#If there are more than 1 record present for nth highest value then sort the key and print the first one,
d={1:20,12:34,3:2,5:45,4:56,9:91,10:67,11:59}
# Sort the dictionary by key values

sorted_lst = sorted(d.items(),key=lambda x:x[1])


n = int(input('Enter the nth value to get the max value '))

for i in range(len(sorted_lst)):
    if len(sorted_lst)<n-1:
        print('the index does not exist in the list')
        break
    else:
        if i == n:
            print (sorted_lst[i][1])


