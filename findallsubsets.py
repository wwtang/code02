"""find all subsets of a set
input "abc"
return [[],"a",'b','c','ab,'ac','bc','abc']
"""


#recursive way

def getsubsets(string):
    
    if len(string) == 0:
        return [[]]
    
    moresubsets = []
    subsets = getsubsets(string[1:])
    
    for subset in subsets:
        moresubsets.append(list(string[0])+subset)

    return moresubsets + subsets

def printsubsets(string):
    result = [''.join(item) for item in getsubsets(string)]

    return result
