"""ex10.6
Question: Given an MxN matrix in which each raw and each colum is sorted in ascending order, write a method
to find an element

*****************************************************
ma[i][j]#i is the raw, j is the colum
observation of the matrix

###(quantify the location of x, not just implicit say yes or no )
1. if the start of a column is greater than x, then x is to the left of this colum
2. if the end of a colmn is lesser than x, then x is to the rigth of this column
3. if the start of a row is greater than x, then x is to the above of the row
4. if the end of a row is lesser than x, then x is to the below of the row

Now according to the observation above, we can begin in many number of places, but begin
from the (end of row, beign of colum) or (begin of row, end of column) will be more efficient
than other places




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


def findElement(ma,x):
    row = 0# begin of row
    col = len(ma[0])-1# end of column

    #please carefully considerate the boundary situsation 
    while row<= len(ma[0])-1 and col >=0:# start from (begin of row, end of column)
        if ma[row][col] == x:
            print "Element %s is located at row %s, col %s"% (x, row, col)
            return True
        elif ma[row][col] > x:
            col -= 1
        else:
            row +=1
    print "The target number %s is not in the matrix" % x
    return None

def main():

    ma = [
            [15,20,40,85],
            [20,35,80,95],
            [30,55,95,105],
            [40,80,100,120]
            ]

    findElement(ma,101)
    findElement(ma,55)
    findElement(ma,15)
    findElement(ma,95)
    findElement(ma,105)
    findElement(ma,100)
    findElement(ma,80)
    findElement(ma,120)


if __name__=="__main__":
    main()
    





    
