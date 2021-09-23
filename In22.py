'''Given a set of characters and a positive integer k, print all possible strings of length k
that can be formed from the given set.

Examples:

Input:
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb'''


##METHOD 1
s,k = {'a', 'b'},3

x = [(i,j,k) for i in s for j in s for  k in s ]

print(x)


print('------------------------------Method 2----------------------')
# possible strings of length k

# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()


def printAllKLength(set, k):
    n = len(set)
    printAllKLengthRec(set, "", n, k)


# The main recursive method
# to print all possible
# strings of length k
def printAllKLengthRec(set, prefix, n, k):
    # Base case: k is 0,
    # print prefix
    if (k == 0):
        print(prefix)
        return

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)


# Driver Code
if __name__ == "__main__":
    print("First Test")
    set1 = ['a', 'b']
    k = 3
    printAllKLength(set1, k)

    print("\nSecond Test")
    set2 = ['a', 'b', 'c', 'd']
    k = 1
    printAllKLength(set2, k)


