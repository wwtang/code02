#Check dupliate element of list with dict

def checkDupDict(l):
    new_d = {}
    for e in l:
        if e not in new_d:
            new_d[e] = 1
        else:
            new_d[e] +=1
    print new_d
    for val in new_d.values():
        print val
        if val > 1:
            print 'The duplicate elemt is:'
            break
        else:
            print 'There is no duplated element'
            
