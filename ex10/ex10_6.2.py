"""ex10_6.2
Question: Given an MxN matrix in which each raw and each colum is sorted in ascending order, write a method
to find an element

*****************************************************
Utilize bianry search to find the target element, the diagonal is well sorted






*****************************************************
ex:
ma = [
        [15,20,40,85],
        [20,35,80,95].
        [30,55,95,105],
        [40,80,100,120]
        ]

    find 55
    output ma[2][1]
"""

def  findElement(ma,x):
    col = len(ma) -1
    row = len(ma[0]) - 1

    # orig and dest should be coordinate not the value
    #orig = ma[0][0]# the origin of  the maxtrix
    #dest = ma[row][col] #the destination of the matrix

    orig = [0,0]
    dest = [col, row]

    return findelement(ma, x, orig, dest)

def findelement(ma, x, orig, dest):

    #check the bound first, dest should larger than origin
    if dest[0] < 0 or dest[1] < 0:
        return None

    if  not isbefore(orig, dest): # orig should be before the dest
        return None

    if ma[orig[0]][orig[1]] == x:
        return orig

    #check the diagnal first, if the target x is not there then search the lowerleft and upperright parts

    #
    startp = orig#[0,0]
    
    # if the matrix is not square, the distance between the col and row is not equal
    diagonalDist = min(dest[0]-orig[0], dest[1]-orig[1] )# the min value of the row distance and col distance

    endp = [startp[0]+ diagonalDist, startp[1]+diagonalDist]

    #find the mid point, THIS SHOULD BE PUT IN THE WHILE LOOP
     #   row_mid = (startp[0] + endp[0])/2
    #col_mid =  (startp[1] + endp[1])/2
    #mid = [row_mid, col_mid]

    #search the diaganla
    ## do the binary search on diagnal, looking for the first element that greater than x
    while isbefore(startp, endp):
        #find the mid point
        mid = find_mid(startp, endp)
        print "while startp", startp
        print "while endp", endp
        print "while mid", mid
        
 #       if ma[mid[0]][mid[1]] == x:
 #            return mid
        #find the first element greater than x, and then goes to lowerright
        if x > ma[mid[0]][mid[1]] :
            #startp[0] += 1
            #startp[1] += 1 not this
            startp[0] = mid[0] +1
            startp[1] = mid[1] +1 # be careful
 
            #return findelement(ma,x, startp, endp)
        # goes to the upperleft
 #       elif x == ma[mid[0]+1][mid[1]+1]:
 #           return [mid[0]+1, mid[1]+1]
        #elif x > ma[mid[0]+1][mid[1]+1]:#goes to the downright 
           # endp[0] -= 1
            #endp[1] -= 1
        else:
           endp[0] = mid[0] -1
           endp[1] = mid[1] -1
 #           return findelement(ma, x, startp, endp)

    print "mid", mid
    print "startp", startp
    print "endp", endp
    #if doesn't find x in the diagol region, goes to the rest reagon
    print "we are here "
    return partitionAndSearch(ma, x, orig, dest, startp)


    
    

#search the lowerleft and upperright part of the coordinate
def partitionAndSearch(ma, x, orig, dest, pivot):
    print "pivot", pivot

    lowerleftorig = [pivot[0], orig[1]]
    lowerleftdest = [dest[0], pivot[1] -1]

    upperrightorig = [pivot[0], orig[1]]
    upperrightdest = [pivot[0] -1, dest[1]]

    print "lowerleftorig", lowerleftorig
    print "lowerleftdest", lowerleftdest

    lowerleft = findelement(ma,x, lowerleftorig, lowerleftdest)
    if lowerleft is None:
        return findelement(ma, x, upperrightorig, upperrightdest)
    
    print "lowerleft", lowerleft
    return lowerleft

def isbefore(start, end):
    return start[0] <= end[0] and start[1] <= end[1]


def find_mid(startp, endp):
    row_mid = (startp[0] + endp[0])/2
    col_mid =  (startp[1] + endp[1])/2
    mid = [row_mid, col_mid]
    return mid

def main():
    ma = [
            [15,20,40,85],
            [20,35,80,95],
            [30,55,95,105],
            [40,80,100,120]
            ]
    
    #print findElement(ma, 15)
    print findElement(ma, 35)
   # print findElement(ma, 95)
   # print findElement(ma, 120)
    

   # print findElement(ma, 55)

if __name__=="__main__":
    main()
    









    
