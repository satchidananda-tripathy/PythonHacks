#Binary Search can be applied on sorted list
'''STEPS
low = 0 and up = index of last element
mid = int((low+up)/2)

if the search element is present at mid location then return mid
if the search element is grater than the mid location then change low to mid +1
if the search element is smaller than the mid location then change upper to mid -1
'''

def bin_srch(lst,srch):
    strt_index = 0
    end_index = len(lst) - 1

    while strt_index <= end_index :
        mid_point = (strt_index + end_index)//2
        if lst[mid_point] == srch:
             return mid_point
        else:
            if lst[mid_point] < srch:
                strt_index = mid_point + 1
            else:
                end_index = mid_point -1
    return None



l = [10,20,30,40,50,60,70,80]
srch = 10

print(bin_srch(l,srch))