def lcs(xs, ys):
    '''Return a longest common subsequence of xs and ys.
    
    Example
    >>> lcs("HUMAN", "CHIMPANZEE")
    ['H', 'M', 'A', 'N']
    '''
    if xs and ys:
        xb = xs[:-1]
        xe = xs[-1]
        yb = ys[:-1]
        ye = ys[-1]
        #*xb, xe = xs
        #*yb, ye = ys
        if xe == ye:
            return lcs(xb, yb) + [xe]
        else:
            return max(lcs(xs, yb), lcs(xb, ys))
    else:
        return []
def main():
    x = "ABCBDAB"
    y = "BDCABA"
    print lcs(x,y)

if __name__=='__main__':
    main()
