# print power set of a set
#power set is the set of all possible subsets of a set which contains pow(2,noofelementsofset) items

#Example :  s={1,2} there are pow(2,2) subsets e.g. {} {1} {2} {1,2}

'''
Logic : Step 1 create an empty set {}
      : Step 2 create one more set and add first element i.e. {1} so the list becomes {} , {1}
      : Step 3 Add next elements to above sets i.e. {2} {1,2} so list becomes  {} {1} {2} {1,2}
      : Continue step 3 untill all elements visited.  This looks like a recursive algorithm
      :So any time we accept a new number we create a new subset and add with the old one
'''

input=[1,2,3]
output=[[]]
for nums in input:
    ## Keep adding the values in the output
    output+=[[nums]+items  for items in output]
print(output)

# explanation initiall nums = 1  so [1] which will be added in [] resulting [] , [1]
# next nums nums = 2 so [2] which will be added in [] and and [1] resulting [] [1] [2] [1,2]  so on

