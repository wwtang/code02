def findDup(l):
    new_d = dict()
    for i in l:
       if i not in new_d:
           new_d[i] =1
       else:
           new_d[i] += 1
    dupitem = dict()
    for item in new_d:
       if new_d[item] > 1:
           dupitem[item] = new_d[item]
           print dupitem.items()
    
    duplist = list(dupitem.keys())
    return duplist
