#If string is 12 Hell 0 abc 1d34
#Expected output is 12,0,1,34
#

sentence = 'Extract 100 100.45 and 10000 from this string'
s = []
for t in sentence.split():
    try:
        s.append(float(t))
    except ValueError:
        pass
print(s)

print('If there is no separator or space from the digits we need to change the logic')

str="12Hell0abcdef1d34"
lst =[]

for chars in str:
    if chars.isdigit():
        lst.append(chars)
    else:
        lst.append('')
print(lst)

#Use unpack operator to get values

print('-------')
sentence = 'Extract 100 100.45 and 10000 from this string'

for x in sentence.split():
   try:
       print(float(x))
   except:
       pass


