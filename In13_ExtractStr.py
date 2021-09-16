from curses.ascii import *

input_str="abcd2315@#&^ef"
#output_str="fedcba1^&#@' i.e. char in rev order then smallest num then symbols in rev order


digits=[chr for chr in input_str if isdigit(chr)]
alpha=[chr for chr in input_str if isalpha(chr)]
digits.sort(reverse=True)
symbols=[chr for chr in input_str if chr not in alpha and chr not in digits]


print(list(alpha[::-1])+list(digits[0]+list(symbols[::-1])))