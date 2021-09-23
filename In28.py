'''
Print minimum absolute difference

Given an array of distinct integers arr,
 find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
'''

arr = [1,3,6,10,15]

pairs =[(a,b) for a in arr for b in arr if a<b]

diff = [b-a for (a,b) in pairs ]
print(min(diff))