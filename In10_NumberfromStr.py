#Extract numbers from String
str="12Hell0abc1d34"
nums=[items for items in str if items.isdigit() ]

print(f"Below is not correct as it is extracting by digits from {str}")
print(nums)


def extract_nbr(input_str):
    if input_str is None or input_str == '':
        return None

    out_number = []
    for ele in input_str.split():
        if ele.isdigit():
            out_number.append(ele)
    return out_number

x=extract_nbr(str)
print(x)