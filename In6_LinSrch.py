# Linear Search
# Scan the list from left to right and return the positon where it is matching. Return -1 if not found
def lin_srch(lst,srch):
    for idx in range(len(lst)):
        if lst[idx] == srch:
            return idx
    else:
        return -1

l = [10,23,20,99,30,40,50,60,121,70,80]
srch = 100

print(lin_srch(l,srch))