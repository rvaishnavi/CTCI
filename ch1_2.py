# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# 1 - Describe what it means for two strings to be permutations of each other.
#     Now, look at that definition you provided. Can you check the strings against that definition?
# 84 - There is one solution that is 0( N log N) time. Another solution uses some space, but is O(N) time.
# 122 - Could a hash table be useful?
# 131 - Two strings that are permutations should have the same characters, but in different orders.
#       Can you make the orders the same?


# By sorting two strings
def is_perm1(str1,str2):
    return sorted(str1) == sorted(str2)


# By character counting
def is_perm2(str1,str2):
    cset = []
    if len(str1) == len(str2):
        for i in str1:
            if i not in cset:
                if str1.count(i) == str2.count(i):
                    cset.append(i)
                else:
                    return False
        return True
    return False

