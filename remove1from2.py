"""

Remove character from the first string which are present in the second string

algorithm

0, initalize a result list
1. build a dict for the second string, 
2. for each character in the first string, lookup the dict, if yes do nothing ,else append it to result

runtimw = o(m+n)
"""

def remove1from2(str1, str2):
    if len(str1) <1 or len(str2) <1:
        return None
    result = []
    str2_dict = dict()

    for char in str2:
        if char not in str2_dict:
            str2_dict[char] = 1
    print str2_dict
    for char in str1:
        if char not in str2_dict:
            result.append(char)
    return result

def main():
    str1= "abcdefg"
    str2 = "abc"

    print remove1from2(str1,str2)

if __name__=="__main__":
    main()
            
        
