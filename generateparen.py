def  addParen(result_list, pro_list, openParen, closeParen):
    # no   result_list = [] here, every time  call of addParen list set to empty
    #can not put  str = [] here, every time str update to []
    if openParen < 0 or closeParen > openParen:
        return False
    if openParen == 0 and closeParen == 0:
        result_list.append(pro_list)
        print result_list, "result list "
        return result_list
    else:
        # add left Paren
        if openParen > 0:
            pro_list.append( "(")
            
            print pro_list
            print "we are here ***"
            addParen(result_list, pro_list, openParen -1, closeParen)
            
            print openParen -1, closeParen," paren numbers"
            
        #add right Paren
        if closeParen > openParen:
            pro_list.append( ")")
            print "we are here *******"
            addParen(result_list, pro_list,openParen, closeParen-1)
            

def generateParen(num):
    result_list = []
    pro_list = []
    addParen(result_list, pro_list, num,num)
def main():
    print "test of the second methods"
    print generateParen(3)

if __name__=="__main__":
    main()
