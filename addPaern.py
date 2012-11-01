"""Print all the valid combiantion of n-pairs of parentheses

1, left Paren: as long as we not used up the left Paren, we can insert a left Paren
2, right Paren: we can insert a right Paren as long as not leading a syntax error

(Catalan Number)
"""

def addParen(lst, left, right, strs, index):
    """lst used to hold final result
        left, right represent the # of left and right parens
        strs used to store temp string during operation
        index represent the postion of new inserted paren in the strs
    """
    if left < 0 or right < left:
        return None

    if left ==0 and right ==0:#the last right paren was inserted, copy the value and append to lst
        newParen = strs[:]#copy strs to newParen
        strs = []
        lst.append(newParen)

    else:
        if left > 0:
            leftstrs = strs[:]
            leftstrs.insert(index, '(')# insert left Paren to strs
            addParen(lst, left -1 ,right, leftstrs, index+1)
            #addParen(lst, left -1 ,right, strs, index+1)

            print "LeftParen: List: %s, Left: %s, Right: %s, strs: %s, index: %s"%(lst, left, right, strs, index)

        if right > left:
            rightstrs = strs[:]

            rightstrs.insert(index, ')')
            addParen(lst, left, right-1, rightstrs, index+1)
           # addParen(lst, left, right-1, strs, index+1)

            print "RightParen: List: %s, Left: %s, Right: %s, strs: %s, index: %s"%(lst, left, right, strs, index)

    return lst

def main():
    lst = []
    strs = []
    #print addParen(lst, 3,3, strs, 0)

    print ["".join(paren) for paren in addParen(lst, 3, 3, strs, 0)]

if __name__=="__main__":
    main()
        
