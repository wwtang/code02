"""
find the longest common subsequence of two string X and Y, return Z

c[[m],[n]]

if i <=0 or j<=0: c[[m],[n]] =0
if X[m] == y[n], c[[m],[n]] = c[[m-1],[n-1]]
if X[m] !=Y[n]:
    if c[[m-1],[n]] >c[[m],[n-1]]: c[[m],[n]] = c[[m-1],[n]]
    else:
        c[[m],[n]] = c[[m],[n-1]]
        

"""
def lcs_len(x, y):
    """this function just returns the length of lcs"""
    if len(x) ==0 or len(y) ==0:
        return 0

    px = x[:-1]
    py = y[:-1]

    if x[-1] ==y[-1]:
        return lcs_len(px,py) +1
    else:
        return max(lcs_len(x,py), lcs_len(px,y))

def main():
    x = "abcde"
    y = "bcd"
    print lcs_len(x,y)

if __name__=="__main__":
    main()
