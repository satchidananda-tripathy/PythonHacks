#Complete a function that returns a list containing all the mismatched words (case sensitive)
# between two given input strings # For example: # - string 1 : "Firstly this is the first string" # - string 2 :
# "Next is the second string" # # - output : ['Firstly', 'this', 'first', 'Next', 'second']

string1 = "Firstly this is the first string"
string2 = "Next is the second string"

s1=set(string1.split())
s2=set(string2.split())

print(list(s1^s2))

# method 2

s1Minuss2 = [word for word in string1.split() if word not in string2.split()]
s2Minuss1 = [word for word in string2.split() if word not in string1.split()]
print(s1Minuss2+s2Minuss1)

print("Question : Given two sentences, construct an array that has the words that appear in one sentence and not the other")

print('Use previous solution for this question')
