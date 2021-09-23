#Write a function to return the number of times a character appears in a string.
# The character can be the empty string

def chr_count(str):
    final_chr = {}
    for chr in str:
        if chr in final_chr:
            final_chr[chr]=final_chr[chr]+1
        else:
            final_chr[chr]=1
    return final_chr

str=input('Enter a String')

if len(str)==0:
    print('The string is empty')
else:

    x=chr_count(str)
    print(x)

    y = [x[i] for i in x]
    print('The counts are ')
    print(y)

    mx = max(y)

    r = [i for i in x if x[i]==mx]

    print(r,'Occurs ' , mx, ' times ')


