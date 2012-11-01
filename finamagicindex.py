"""Find the magic index in a list  that a[i] = i, use the binary search algorithm

BST problem
1. ordered data (if not sorted if first)
2. apply BST
"""


def findMagicIndex(argv, start,end):
    if start<0 or start>end or end>len(argv) :
        return False
 
    mid = (start+end)/2
    if argv[mid] == mid:
        #print mid
        return mid
        
    elif argv[mid] < mid:
       
        #print "*",argv, mid+1,end,"*"
        return findMagicIndex(argv, mid+1, end)
        
    else:
        
        return findMagicIndex(argv, 0 ,mid-1)

def MagicIndex(argvlist):
    return findMagicIndex(argvlist, 0, len(argvlist))


def main():
    print "start"
    print   MagicIndex([-40,-20,-1,1,2,3,5,7,8,12,13])
    print "end"

if __name__=="__main__":
    main()
