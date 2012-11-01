"""Wirte a method to determine if the second string is a rotation of the 1st string

algorithm

1. build a temp string as str1+str1
2. if the 2nd str is a substring of str1+str1, return true
else return flase


"""


def ifRotation(str1, str2):

    if len(str1)<1 or len(str2) < 1:
        return False

    tmp = str1+str1

    if str2 in tmp:
        return True
    return False

def main():
    str1= "abacd"
    str2 = "cdaba"

    print ifRotation(str1,str2)

if __name__=="__main__":
    main()
