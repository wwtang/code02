"""
ex9_6 Print all the valid combination of n-pairs parentheses


input the number of piars of parentheses
return a list of list

"""

def printParen(n):
    if n == 0:
        return None
    
    if n ==1:
        return [["(",")"]]
    
    result = []
    for paren in printParen(n-1):
        for index, sym in enumerate(paren):
            if sym == '(':
                #newp = paren# assign directly will operate on the orignial paren
                newp= paren[:]
                newp.insert(index+1, '(')
                newp.insert(index+2, ')')
                
                #print "insert right", newp
                #print "*"*3
                #print "paren", paren
                #print "*"*3
                if newp not in result:
                    result.append(newp)
                #print "result here", result
                newp = []                
                #print "result",result
        paren.insert(0, '(')
        paren.insert(1, ')')
  
        result.append(paren)

    return result

def printParen2(left, right, result):
    if left ==0 and right ==0:
        return result
    if left > 0:
        result.append("(")
        return printParen2(left -1, right+1, result)
    if right > 0:
        result.append(")")
        return printParen2(left, right -1, result)
    

def addParen(lst, left, right, strs, count):
    if left < 0 or right < left:
        return None
    if left ==0 and right ==0:
        newstr = strs[:]
        strs = []
        lst.append(newstr)
    else:
        if left > 0:
            strsLeft =strs[:]
            strsLeft.insert(count, '(')
            print 'left addpare lst: %s, left:  %s right: %s strs: %s, count: %s'%(lst,left,right,strs,count+1)
            addParen(lst, left -1, right, strsLeft, count+1)

        if right > left:
            strsRight = strs[:]

            strsRight.insert(count, ')')
            print 'right addpare lst: %s, left:  %s right: %s strs: %s, count: %s'%(lst,left,right,strs,count+1)
            addParen(lst, left, right -1, strsRight, count+1)

    return lst

def main():
    print ["".join(paren) for paren in printParen(2)]
    print ["".join(paren) for paren in printParen(3)]
    #result = []
    #print printParen2(3,3, result)
    lst = []
    strs = []
    print addParen(lst, 2, 2, strs, 0)


if __name__=="__main__":
    main()
            
            
