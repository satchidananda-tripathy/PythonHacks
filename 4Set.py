#Unordered so can not fetch items by position, can not contain dups, Normally set is mutable but frozen set is not mutable
#s={} it is not an empty set , it is a dictionary
#s=set() it is an empty set
#it has operations like union intersection diff and complement
######################
# IMP can not keep mutable objects like list, dictionary within set but we can keep string, tuples etc.
# Immutable version of a python set is known as Frozen set
#f=frozenset() .. f.add() will raise exception . Hence it can be used a keys in a dictionary

print('Output of below and operation is an empty set represented as set()')
print({1,2,3}&{'abc'})

a={1,2,3,4}
b={4,5,6,7}
c={1,4,9}
print("output of b -a-c is : ")
print(b.difference(a,c))
print('-------------------')
x,y={1,3,5,7},{2,4,6,8}
print('There is no common elements between set x and y : ', end='')

print(x.isdisjoint(y))

print(''' below are few commonly used functions in Sets 
    Union | a.union(b)
    Intersection & a.intersection(b)
    difference -   a.difference(b)
    Symmetric difference ^ a.symmetric_difference(b) means (a-b)union(b-a)
    Subset a<=b  a.issubset(b)
    Superset a>=b a.issuperset(b)''')


