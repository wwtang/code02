"""ex1.2 reverse a c/c++ style string, which reverse a null-terminated string

algorithm:

initialize two index i and j, i begins from the starts, j begins from the ends

befor i == j
swap string[i] and string[j]
i ++
j --

"""
#the end of string is ""
def reverseStr(string):
    if len(string) <2:
        return string
    i = 0
    j = len(string) -1
    lst_str = list(string)
    while i < j:
        lst_str[i], lst_str[j] = lst_str[j], lst_str[i]
        i +=1
        j -=1
    return "".join(lst_str)

#recursive method
def reverseStr2(string):
    if len(string) <=1:
        return string
    return string[-1] + reverseStr2(string[:-1])
def main():
    strings = ["", "a ", "abcd ", "asdf",'abcde']
    print [reverseStr(string) for string in strings]
    print "Recursive way"
    print [reverseStr2(string) for string in strings]

    

if __name__=="__main__":
    main()
    
