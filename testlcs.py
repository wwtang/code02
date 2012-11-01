""" lcs"""


def lcs(x,y):
    m = len(x)
    n = len(y)
    c = []
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j ==0:
                print i,j
                print x[i], y[j]
                c[i][j] = 0
            elif x[i] == y[j]:
                c[i][j] = c[i-1][j-1]
            elif x[i] != y[j]:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    return c


def main():
    x = "abcd"
    y = "bcde"
    lcs(x,y)

if __name__=="__main__":
    main()

    
    
