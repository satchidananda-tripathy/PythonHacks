#Extract numbers from String
str="12Hell0abc1d34"
nums=[items for items in str if items.isdigit() ]

print(f"Below is not correct as it is extracting by digits from {str}")
print(nums)

print('----------Method 2------')
def extract_nbr(input_str):
    out_number = []
    if input_str is None or input_str == '':
        return out_number

    for ele in input_str:
        if ele.isdigit():
            out_number.append(ele)
    return out_number

x=extract_nbr(str)
print(x)