#Write a function to return the number of times each character appears in a string
# and print the char repeated highest no of times
def prntChr(sentence):
    char_freq={}
    for char in sentence:
        if char in char_freq:
            char_freq[char]+=1
        else:
            char_freq[char]=1
    return char_freq

statement = "Hello boys how are you doing"
char_frequency=prntChr(statement)

lst=[]
for cnts in char_frequency.values():
    lst.append(cnts)

for chrs in char_frequency:
    if char_frequency[chrs]==max(lst):
        print(f"The character : {chrs} gets repeated : {max(lst)} number of times")
        break



