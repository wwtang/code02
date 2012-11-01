"""find all the valid parentheses
input: number of pairs of parentheses
output : a list of valid parenthese, left and right are separated.

each function implement the most basic functionality

The first algorithm takes o(n!) n' factorial, which is the b
"""

# i is the index of the open parentthese

# string is a list
def insertParenthese(string, i):
    return string[:i+1] +["("]+[")"]+string[i+1:]

def findParenthese(num):
    parenthese = []
    if num == 0:
        return [[]]
    if num == 1:
        parenthese  = [["(",")"]]
        return parenthese
    else:
        pre_result  = findParenthese(num-1)
        # item is a list
        for item in pre_result:
            # element of the list
            for i in range(len(item)):
                if item[i] =="(":
                    new_result = insertParenthese(item,i)
                    # remove the duplicated item
                    if new_result not in parenthese:
                        parenthese.append(new_result)
                        # add the "()" at the beigning if "()" not there
            if ["(",")"] + item not in parenthese:
                parenthese.append(["(",")"]+item)
        return parenthese
        
# more efficient method
def  addParen(result_list, pro_list, openParen, closeParen, count):
    # no   result_list = [] here, every time  call of addParen list set to empty
    #can not put  str = [] here, every time str update to []
    if openParen < 0 or closeParen > openParen:
        return False
    if openParen ==0 and closeParen ==0:
        result_list.append(pro_list)
        print result_list, "result list "
        return result_list
    else:
        # add left Paren
        if openParen > 0:
            pro_list.append( "(")
            print pro_list
            print"we are here ***"
            addParen(result_list, pro_list, openParen -1, closeParen, count +1)
            print openParen -1, closeParen," paren numbers"
            print count,"count"
        #add right Paren
        if closeParen > openParen:
            pro_list.append( ")")
            print "we are here *******"
            addParen(result_list, pro_list,openParen, closeParen-1, count+1)
            

def generateParen(num):
    result_list = []
    pro_list = []
    addParen(result_list, pro_list, num,num,0)
    print "come here"
    return result_list
            
        

def main():
    print findParenthese(0)
    print findParenthese(1)
    print findParenthese(2)
    print "for 3"
    p = findParenthese(3)
    for elem in p:
        s = "".join(elem)
        print s
    print "test of the second methods"
    print generateParen(2)

if __name__=="__main__":
    main()
