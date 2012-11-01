def numToRomanNum(Num):
    if Num < 1 or Num > 3999:
         print 'The Num must in 1-3999'
    else:
        NumDic = {
             '1':('I','IV','V','IX'),
             '2':('X','XL','L','XC'),
             '3':('C','CD','D','CM'),
             '4':('M')
             }        
        items = sorted(NumDic.items())#dict is unordered
        print items
        retstr = ''
        for item in items:
            str = ''
            (Num,modNum) = divmod(Num,10)#check for the ones digit
            print Num
            if modNum != 0:
                if item[0] != '4':# case for thousands 
                    print '$$'
                    print item[0]
                    if modNum <= 3:
                        while modNum > 0:# concatenate the one roman string from 1 to 3
                            str = str.join(['',item[1][0]])
                            print '#'
                            print str
                            print '#'
                            modNum -= 1
                    elif modNum < 5: # check the 4
                        str = item[1][1]
                        print 'check the 4'
                        print str
                    elif modNum == 5:#check the 5
                        str = item[1][2]
                        print 'check the 5'
                        print str
                    elif modNum < 9: #check 6-8
                        str = item[1][2]
                        while modNum > 5:
                            str = str.join(['',item[1][0]])
                            print 'check 6-8'
                            print str
                            modNum -= 1
                    else:                   #check 9
                        str = item[1][3]
                else: 
                    while modNum > 0:#case for thouands 
                        str = str.join(['',item[1][0]])
                        modNum -= 1
                retstr = str.join(['',retstr])
        return retstr
