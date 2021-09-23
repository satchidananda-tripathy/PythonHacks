#print even numbers between 100 using list comprehension

print('Even numbers bet 100')
even=[n for n in range(2,100,2)]
print(even,end=',')

print('or')
even=[n for n in range(100) if n%2==0]
print(even,end=',')

print('Even square of no bet 1 to 10')
sq=[n*n for n in range(11)]
print(sq)

print('Movies start with Da')
# print movies whose names starts with  with Da
movies=['Dalal','Dasaan','Aag','Bagban','Khiladi']
outMovies=[ m for m in movies if m.startswith('Da') ]
print(outMovies)

print('Movies released befor 2000 from below list of tuples')
movies=[(1996,'Dalal'),(2004,'Dasaan'),(1998,'Aag'),(2006,'Bagban'),(1997,'Khiladi')]

old_movies=[m_names for (year,m_names) in movies if year<2000]
print(old_movies)

print('or')
old_movies=[m_names[1] for m_names in movies if m_names[0]<2000]
print(old_movies)

print('Multiply each number of a list by 10')
v=[1,2,3,6,7]
r=[item*10 for item in v]
print(r)
#########################################  Important question with less code ##########
print('Cartician Products of two sets ')
S1={1,2,3}
S2={'a','b','c'}


l1=list(S1)
l2=list(S2)

C=[(x,y) for x in l1 for y in l2 ]
print(set(C))






