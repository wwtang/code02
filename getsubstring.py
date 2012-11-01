"""find all the substring of a string(continus )

two methods
recursive

and

straight 
"""
#recursive, efficient for distinctive string t(n) = t(n-1) + o(n^2) = o(n^3)

def getsubstr(string):
    if len(string) == 0:
        return ['']
    if len(string) == 1:
        return [string]
    
    result = []
    sub_substr = getsubstr(string[1:])
    new_substr = [string[0]]#remenber to add the new char
    nextchar = string[1]#new substr contains the new added char, and the new char prior to the string[1]
    for substr in sub_substr:
        if substr[0] == nextchar:
            new_substr.append(string[0]+substr)
    result = list(sub_substr) + new_substr
    
    return result



#straight, efficient for all the situation o(n^2)

def getsubstr2(string):
    if len(string) < 2:
        return [string]
    j = 1# the gap index for appending new substr
    sub_str = []

    while True:
        for i in range(len(string) - j + 1):#
            sub_str.append(string[i:i+j])# string[len-1:len] returns string[len-1]
        if j == len(string):
            break
        j +=1#increment the gap
    return sub_str

def test(got1, got2):
    if sorted(got1) == sorted(got2):
        print "OK, they work fine"
    else:
        print "got1", got1
        print "got2", got2
        
def main():
    print "For distinctive string"
    string = "abcd"
    test(getsubstr(string),getsubstr2(string))

    print"Now for not  distinctive string: abbd"
    string = "abbd"
    test(getsubstr(string), getsubstr2(string))

if __name__=="__main__":
    main()
    




        
