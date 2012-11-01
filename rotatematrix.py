def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n/2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            top = matrix[first][i]#save the top, similar to the temp

            #left to top
            matrix[first][i] = matrix[last -i-first][first]

            #bottom to left
            matrix[last - i - first][first] = matrix[last][last -i-first]
            #right to bottom
            matrix[last][last-i-first] = matrix[i][last]
            #top to right
            matrix[i][last] = top 
    return matrix


def setZero(matrix):
    #flags the postion which has 0
    n = len(matrix)
    m = len(matrix[0])
    row = [0]*n#for the row and col list as ZERO
    col = [0]*m
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] ==0:
                row[i] = 1
                col[j] = 1
                
    #set matrix[i][j] = 0 if either row i or colum j has 0
    for row_e in row:
        for col_e in col:
            if row_e ==1 or col_e ==1:
                matrix[row_e] = 0
                matrix[row_e][col_e] = 0
    return matrix



def loop_matrix(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print m[i][j]
                
