# Guess the output , before checking the result
str='Python'
print(str[:])
print(str[:2])
print(str[3:-1])
print('-------------------')
print('Interesting it will print every second char')
print(str[::2])

print('Interesting it will print every third char')
print(str[::3])

print('Interesting it will reverse the string')
print(str[::-1])

print('Interesting it will print every second after reversing')
print(str[::-2])

print('Interesting it will reverse and print every 3rd after reversing again')
print(str[::-1][::-3])

