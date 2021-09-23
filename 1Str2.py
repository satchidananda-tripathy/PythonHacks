str='python'
print(str*2)
print('-------------')
print(str*-2)
print('above is the string with length -2 or 0')
print('-------------')
print(str*0)
print('above is the string with length 0')
print('-------------')

print("Below converted every starting letter of word to Cap , also did for 2 as it is not a char.. it assume as delim")
str1='abc def2pqr'
print(str1.title())
print('-------------')


print("Below will throw error because string is immutable")
str[3]='to'
print(str)