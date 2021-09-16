print('append only add one items but extends can add multiple into a list')
lst=[]
lst.append('a')
lst.extend([7]+['a','b',9])
print(lst)
print('-----------')
print('Below example appended the second list as a single element')
lst=[]
lst.append('a')
lst.append([7]+['a','b',9])
print(lst)
print('-----------')
print('VERY TRICKY QUESTIONS ')
R=[1,2,3,4,1]
for items in R:
    R[items]=0
print(R)
print('How did above happened')
print('----EXPLANATION-------')
print(''' In the first iteration the value of R[1] became 0 i.e. it became 1, 0, 3, 4,1
          In the second iteration the value or R[0] becomes 0 because second element became 0 now, so it is 0 0  3 4 1
           Now R[3] becomes 0 .. next R[0] and then R[1] becomes 0''')
print('------------------------------')
print('VERY TRICKY QUESTIONS ')
R=[[0]*2]*2
print('After step 1')
print(R)
print('Here R[0,0],R[0,1],R[1,0],R[1,1] ARE  : ',end='')
print(R[0][0],R[0][1],R[1][0],R[1][1])
print('So the output of print(R[0][0]+R[1][0]) after R[0][0]=1 is  : ',end='')
R[0][0]=1
print(R[0][0]+R[1][0])
print('Are you thinking it should be 1 ?')
print('Here value of R[0][0]+R[1][0] are : ',end='')
print(R[0][0],R[1][0])
print('because when we multiplied R=[[0]*2]*2 they referrenced same memory')

