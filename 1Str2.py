# Guess the output , before checking the result
str='python'
print(str*2)
print('-------------')
print(str*-2)
print('above is the string with length -2 or 0 so it will nullify the string')
print('-------------')
print(str*0)
print('above is the string with length 0')
print('-------------')

print("Below converted every starting letter of word to Cap , also did for 2 as it is not a char.. it assume as delim")
str1='abc def2pqr'
print(str1.title())
print('-----few functions --------')

print(str1.upper())
print(str1.islower())
print(str1.isalpha())
print(str1.isdigit())



print("Below will throw error because string is immutable")
print('------------------------------')
print('------------------------------')
str[3]='to'
print(str)