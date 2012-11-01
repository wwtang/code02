"""Implement an algorithm to determine if a string has alll unique characters.
What if you can not use additional data stucture

Algorithm:
1 use two index i and j go through the string, where i begins at the next character of j.
if string[i] == stirng[j]
return False
else return True

"""

def checkUnique(string):
    """ if all characters are unique return False, else return True"""
    str_len = len(string)

    if str_len == 0:
        return False
    if str_len == 1:
        return True

    for i in range(str_len-1):
        for j in range(i+1, str_len -1):
            if string[i] == string[j]:
                print "string[i] %s and string[j] %s" % (string[i], string[j])
                return False
    return True

#create boolean array of 256
def checkUnique2(string):
    if len(string) ==0:
        return False
    check_table = [None]*256#represents the ASCII value table
    for char in string:
        if check_table[ord(char)]:# if ord(char) exist in table, return false
            return False
        else:
            check_table[ord(char)] = 1
    
    return True

def main():
     strings = ['', 'a', 'aaa','sdf','adfasdf']
     print [checkUnique(string) for string in strings]
     print [checkUnique2(string) for string in  strings]

if __name__=="__main__":
    main()
