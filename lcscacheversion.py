""" def memoize(fn):
    '''Return a memoized version of the input function.
    
    The returned function caches the results of previous calls.
    Useful if a function call is expensive, and the function 
    is called repeatedly with the same arguments.
    '''
    cache = dict()
    def wrapped(*v):
        key = tuple(v) # tuples are hashable, and can be used as dict keys
        if key not in cache:
            cache[key] = fn(*v)
        return cache[key]
    return wrapped


def lcs(xs, ys):
    '''Return the longest subsequence common to xs and ys.
    
    Example
    >>> lcs("HUMAN", "CHIMPANZEE")
    ['H', 'M', 'A', 'N']
    '''
    @memoize
    def lcs_(i, j):
        if i and j:
            xe, ye = xs[i-1], ys[j-1]
            if xe == ye:
                return lcs_(i-1, j-1) + [xe]
            else:
                return max(lcs_(i, j-1), lcs_(i-1, j), key=len)
        else:
            return []
    return lcs_(len(xs), len(ys))
"""
def memorize(fn):
    cache = dict()
    def wrapped(*v):
        key = tuple(v)
        #print "key", key
        #print "cache", cache
        if key not in cache:
            print "new key", key
            cache[key] = fn(*v)
            return cache[key]
    return wrapped


def lcs(x, y):
    @memorize
    def lcs_(i, j):
        if i and j:
            xe, ye = x[i-1], y[j-1]
            if xe == ye:
                print "xe: %s "% xe
                print "i: %s , j: %s "%(i, j)
                return lcs_(i-1,  j-1) + [xe]
            else:
                return max(lcs_(i, j-1), lcs_(i-1, j ))
        else:
            return []
    return lcs_(len(x), len(y))




def main():
    x = "ABCBD"
    y = "BCR"
    print lcs(x,y)

if __name__=="__main__":
    main()
    
