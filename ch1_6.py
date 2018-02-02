# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# 92 - Do the easy thing first. Compress the string, then compare the lengths.
# 110 - Be careful that you aren't repeatedly concatenating strings together. This can be very inefficient.


def string_compress(string):
    clist = []
    count = 1
    length = len(string)
    if length > 2:
        for i, v in enumerate(string[1:]):
            if count == 1:
                clist.append(string[i])
            if string[i] == v:
                count +=1
            else:
                if count >1:
                    clist.append(str(count))
                count =1
                if i+2 == length:
                    clist.append(v)
        if count > 1:
            clist.append(str(count))
    return ''.join(clist) if len(clist) < length and len(clist) >0  else string

if __name__ == "__main__":
    print(string_compress("abccddeeffa"))