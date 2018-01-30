# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


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

