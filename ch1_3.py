# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

# 53 - It's often easiest to modify strings by going from the end of the string to the beginning.
# 118 - You might find you need to know the number of spaces. Can you just count them?

# https://stackoverflow.com/questions/8798403/string-is-immutable-what-exactly-is-the-meaning
# https://stackoverflow.com/questions/9097994/arent-python-strings-immutable-then-why-does-a-b-work


# with O(n) time and space complexity
def urlify(string, truelength):
    return string[:truelength].replace(' ', '%20')


# with O(n) time and space complexity
def urlify2(string, truelength):
    return ''.join('%20' if c == ' ' else c for c in string[:truelength])


'''
# String immutable in python - 
# with O(n) time and O(1) space
def urlify3(string, truelength):
    length = len(string)
    while(truelength>0):
        if string[truelength] != " ":
            string[length-1] = string[truelength-1]
            length -=1
            truelength -=1
        else:
            string[length-4:length-1] = '%20'
            length -= 3
    return string
'''

'''
if __name__ == "__main__":
    print(urlify2("Mr John Smith    ",13))
'''