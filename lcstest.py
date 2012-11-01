"""dynamic programming lcs"""

def lcs(x,y):
    n  = len(x)
    m = len(y)

    table = {}

    subsex = []
    subsey = []
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j ==0:
                table[i, j] = 0
                #print "table", table
            
            
            elif x[i-1] == y[ j-1]:# i range (1....n) if i = n , then i- 1 = n-1, which is the last elem of x
                print "x[i-1]:  %s,  y[i-1]: %s : "%(x[i-1],y[j-1])
                
                subsex.append(x[i-1])
                subsey.append(y[j-1])
                table[i, j] = table[i-1, j-1] +1
            else:
                table[i , j] = max(table[i-1,j], table[i, j-1])
    for k,v in table.items():
        if v:
            print k, v
    print subsex
    print subsey
    #return table

    def recon(i, j):
        if i ==0 or j ==0:
            return []
        elif x[i-1] ==y[j-1]:
            return recon(i-1,j-1) + [x[i-1]]
        elif table[i-1, j ] > table[i, j-1]:
            return recon(i-1,j)
        else:
            return recon(i, j-1)
    print "look here"
    return recon(n, m)

def main():
    x = "ABCBDAB"
    y = "BDCABA"
    print lcs(x,y)

if __name__=='__main__':
    main()


                
