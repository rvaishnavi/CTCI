# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

# 23 - Start with the easy thing. Can you check each of the conditions separately?
# 97 - What is the relationship between the "insert character" option and the "remove character" option?
#       Do these need to be two separate checks?
# 130 - Can you do all three checks in a single pass?


def oneeditaway(first, second):
    if abs(len(first)-len(second)) >1:
        return False
    if len(first)<len(second):
        s1, s2 = first, second
    else:
        s1, s2 = second, first

    index1, index2 = 0,0
    diff = False

    while (index1<len(s1)) and (index2 <len(s2)):
        print(index1,index2)
        if s1[index1] != s2[index2]:
            if diff:
                return False
            diff = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True

'''
if __name__ == "__main__":
    print(oneeditaway("pale","pkle"))
'''
