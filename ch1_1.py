# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

#import sys


# Assuming ASCII character set
# Using Dictionary : Time complexity O(n) and a space complexity O(1)
def is_unique1(string):
    if len(string) > 128:
        return False
    sdict = {}
    for i in string:
        if i in sdict:
            return False
        sdict[i] = True
    return True


# Using set
def is_unique2(string):
    return len(string) == len(set(string))


# Using Bit vector if the string contains only lowercase
def is_unique3(string):
    checker = 0
    for i in string:
        val = ord(i) -ord('a')
        if (checker & (1<<val))>0:
            return False
        checker |= (1<<val)
    return True


# With no additional data structure - O(n*n) time complexity and O(1) space
def is_unique4(string):
    for i, v in enumerate(string):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True


# With no additional data structure - sort and linear check - O(n log n)
def is_unique5(string):
    string = sorted(string)
    for i,v in enumerate(string[:-1]):
        if v == string[i+1]:
            return False
    return True


'''
if __name__ == "__main__":
    string = input('Enter string:')
    #string = sys.stdin.readline()
    print(is_unique1(string))
'''