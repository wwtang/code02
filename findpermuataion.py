""" the example of find permutaion """

# prefix ="" . cool why we need the prefix
def getPermutations(string, storage, prefix=""):
    if len(string) ==1:
        # here is prefix + ""stirng"", not "string[i]", each time update the prefix
        storage.append(prefix+string)
    else:
        for i in range(len(string)):
            getPermutations(string[:i]+string[i+1:], storage, prefix+string[i])
            #print "***", prefix+string[i], "***"
    return storage


def getPermutations1(string, prefix=""):
    if len(string) ==1:
        yield prefix + string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations1(string[:i]+string[i+1:], prefix+string[i]):
                yield perm

                
# without a accumulator
def getPermutations2(string, prefix=""):
    if len(string) == 1:
        yield string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations2(string[:i]+string[i+1:], prefix+string[i]):
                yield string[i]+perm

def main():
    print "Version 1 *******"
    storage = []
    getPermutations("abc", storage)
    for permutation in storage:
        print permutation
    print "Version 2 *******"
    p1 =  getPermutations1("abc")
    for item in p1:
        print item
    print p1
    
    print "Version 3 *******"
    p2 =  getPermutations2("abc")
    for item in p2:
        print item
    print p2
    
if __name__ =="__main__":
    main()


