#Given two sentences, you have to print the words those are not present in either of the sentences.
#(If one word is present twice in 1st sentence but not present in 2nd sentence then you have to print that word too)

sentence1="Hello How are you"
sentence2="Hello I am doing good  How about you"
set1=set(sentence1.split())
set2=set(sentence2.split())
print(set1.symmetric_difference(set2))
print('or')
print(set1^set2)

print('------Without using Set------')
# Without using Set
sentence1="Hello How How are you"
sentence2="Hello I  am I doing good How about you"

s1Ms2,s2Ms1=[],[]
for words in sentence1.split():
    if words in sentence2.split():
        pass
    else:
        s1Ms2.append(words)

for words in sentence2.split():
    if words in sentence1.split():
        pass
    else:
        s2Ms1.append(words)
print(set(s1Ms2+s2Ms1))
print('---------------')
print('Method 3')
sentence1="Hello How How are you"
sentence2="Hello I  am I doing good How about you"
s1ms2 =[w for w in sentence1.split() if w not in sentence2.split()]
s2ms1=[w for w in sentence2.split() if w not in sentence1.split()]
print(s1ms2+s2ms1)
