'''Find the duplicate element of sequence'''

def find_dup(s):
    new_d = dict()
    for c in s:
        if c in new_d:
            new_d[c] +=1
        else:
            new_d[c] =1
    dup_dict = dict()
    print
    print new_d
    print
    
    for c in new_d:
        if new_d[c] > 1:
            dup_dict[c]  = new_d[c]
    return dup_dict

def findDupSet(s):
    dupstr = set()
    for i in s:
        if i in s:
            dupstr.add(i)
    print dupstr
    return list(dupstr)
def findD(s):
    uniqueList = []
    dupList=  []
    for i in s:
        if i not in uniqueList:
            uniqueList.append(i)
        else:
            dupList.append(i)
    return dupList
        
