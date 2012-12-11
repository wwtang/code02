"""merge  ordered seqence
input ; tow ordered list
output: merge list of these tow list
"""


def mergeSq(sq1, sq2):
    index1  = len(sq1) -1
    index2 = len(sq2) -1
    #merge index
    indexm = len(sq1) +len(sq2) -1
    sq1 = sq1+ sq2
    print index1,index2,indexm
    

    while index1 >= 0 and index2 >= 0:
        if sq1[index1] >sq2[index2]:
            sq1[indexm]  = sq1[index1]
            index1 -= 1
            indexm -= 1
        else:
            sq1[indexm] = sq2[index2]
            index2 -=1
            indexm -=1
    # copy remaining elements from b into place
    while index2>=0:
        sq1[indexm] = sq2[index2]
        indexm -=1
        index2 -=1
    return sq1

def test(got, expect):
    if got == expect:
        print "Ok"
    else:
        print "No"
        print "got:", got, "expect:", expect

def main():
    test(mergeSq([1,2,3,4,5,6,7,8],[2,3,4]),[1,2,2,3,3,4,4,5,6,7,8])
    test(mergeSq([1,2,6,7,8],[3,4]),[1,2,3,4,6,7,8])
    test(mergeSq([1,2,3,4,5,6,7,8],[9,10,11]),[1,2,3,4,5,6,7,8,9,10,11])

if __name__ =="__main__":
    main()
            
    
