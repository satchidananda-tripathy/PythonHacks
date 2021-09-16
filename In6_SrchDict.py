# Sort a list and print , Use predefined function
#list.sort(key=None, reverse =False) Default property of sort function.

lst =[1,3,2,5,6,8]
print('List sorted in ascending order')
lst.sort()
print(lst)
print('List sorted in descending order')
lst.sort(reverse=True)
print(lst)

### Real life example
#format (name, radius, density, distance from sun)

planets = [
    ("Mercury",10,20,30),
    ("Venus",11,21,31),
    ("Mars",12,22,33),
    ("Jupiter",16,29,23),
    ("Saturn",15,26,39)
    ]

print('Value in the planets')
print(planets)

size = lambda planet : planet[1]
planets.sort(key=size, reverse=True)
print(planets)

density=lambda planet: planet[2]
dist=lambda planet: planet[3]
