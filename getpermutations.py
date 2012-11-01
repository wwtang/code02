"""
find all the permuatation of a string
permutation of string can be derived from permutation of string[1:] by insert the first char at every
spots of the permutation of string[1:]


insertchar

"""

def getpermutation(string):
    if len(string) == 0:
        return [""]

    first = string[0]

    remainders = getpermutation(string[1:])
    result = []
    for remainder in remainders:
        for i in range(len(remainder)+1):
            newstr = insertchar(remainder, first, i)

            result.append(newstr)


    return result

def insertchar(string, char, index):
    start = string[0:index]
    end = string[index :]
    return start + char + end
            
    
    

    
    
