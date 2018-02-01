# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# 106 - You do not have to-and should not-generate all permutations. This would be very inefficient.
# 121 - What characteristics would a string that is a permutation of a palindrome have?
# 134 - Have you tried a hash table? You should be able to get this down to 0( N) time.
# 136 - Can you reduce the space usage by using a bit vector?


def palindrome_perm(string):
    flag = ''
    for i in string:
        if i != ' ' and string.lower().count(i)%2 !=0:
            if flag == '':
                flag =i
            else:
                if flag !=i:
                    return False
    return True


# using dictionary (hash table)
def palindrome_perm2(string):
    odd = 0
    dict = {}
    for i in string.lower():
        if i != ' ':
            if i in dict:
                dict[i]= dict[i]+1
                if dict[i] %2 ==1:
                    odd +=1
                else:
                    odd -=1
            else:
                dict[i]=1
                odd +=1
    return odd <=1


'''
if __name__ == "__main__":
    print(palindrome_perm2("Tact Coa"))
'''