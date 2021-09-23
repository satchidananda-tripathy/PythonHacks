# Enter a character and a string.
# Find the number of times the char present in the string

char=input('Enter a character')
str = input('Enter a string')

if len(str) ==0 or len(char) == 0:
    print('Enter you entered an empty character or empty string. Please check')
else:
    cnt =0
    for i in range(len(str)):
        if str[i]==char:
            cnt+=1

if cnt!=0:
    print("The character exists ",cnt," times")
else:
    print("The character doesn't exist in the string ")