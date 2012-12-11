"""quicksort2
use partition funciton
"""

def qsort2(list):
    if list == []:
        return []
    else:
        pivot = list[0]
        # remember this sentence
        lesser, equal,greater = partition(list[1:], [] ,[pivot], [])
        return lesser +[equal] + greater

def partition(list, l,e,g):
    if list = []:
        return (l,e,g)
    else:
        head = list[0]
        if head < e[0]:
            return partition(list[1:], l+[head], e, g)
        elif head> e[0]:
            return partition(list[1:], l, e, g+[head])
        else:
            reutrn partition(list[1:], l, e+[head], g)

def partition1(list,l,e,g):
    while list !=[]:
        head = list.pop(0)
        if head < e[0]:
            l = [head] +l
        elif head>e[0]:
            g = [head]+g
        else:
            e = [head]+e
        return (l, e, g)
            
