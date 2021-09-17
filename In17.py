#Complete a function that returns the number of times a given character occurs in the given string.
# For example:
# - input string = "mississippi"
# - char = "s"
#
# - output : 4

def cnt_char(st,chr):
    cnt=0
    for i in range(len(st)):
        if chr==st[i]:
            cnt+=1

    return cnt

nput_string = "mississippi"
chr = "s"

print(cnt_char(nput_string,chr))

