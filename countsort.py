"""count sort"""

# k is the range of element in the lst
def count_sort(lst, k):
    b = [0 for i in range(len(lst))]
    c = [0 for i in range(k+1)]
    #initialize c
    # value in c equals the number of element in lst
    for i in xrange(0, len(lst)):
        c[lst[i]] += 1
    # value in c equals or less than the element in lst
    for i in xrange(1, k+1):
        c[i] += c[i-1]

    for j in xrange(len(lst)-1, -1, -1):
 #       tmp = lst[j]
##        b[tmp1]   = tmp
#        c[tmp] -= 1
        b[c[lst[j]]-1] = lst[j]
        
        c[lst[j]] = c[lst[j]]-1
        print "current b: ", b, len(b)
        
    return b

    
def main():
    lst = [6,0,2,0,1,3,4,6,1,3,2]
    l = [2,5,3,0,2,3,0,3]
    print count_sort(l,5)

if __name__=="__main__":
    main()
