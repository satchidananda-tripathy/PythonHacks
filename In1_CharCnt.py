str="Hello How are you I am doing great"

def chr_count(str):
    final_chr = {}
    for chr in str:
        if chr in final_chr:
            final_chr[chr]=final_chr[chr]+1
        else:
            final_chr[chr]=1
    return final_chr

x=chr_count(str)
print(x)

y = [x[i] for i in x]
print('The counts are ')
print(y)

mx = max(y)

r = [i for i in x if x[i]==mx]

print(r,'Occurs ' , mx, ' times ')




