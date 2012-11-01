def numToRomanNum(Num):
    if Num < 1 and Num >3999:
        print 'Num must be in 1-3999'
    else:
        NumDic = {
            '1' : ('I','IV','V','IX'),
            '2' : ('X','XL','L','XC'),
            '3' : ('C', 'CD','D','CM'),
            '4' : ('M')
            }
        items = sorted(NumDic.items()) # sort the unorederd dict keys used for 'for ' loop
        retstr=''
        for item in items:
            str = '' # together with the ' retstr =str.join()' loop one time, store the Roman Char 
            (Num,modNum) = divmod(Num,10) # check from the ones
            if modNum !=0:
                if item[0] != '4': #confused.  how would I know what item[0] is?,
                    # every time, the 'item' have the 'item[0] = index' and 'item[1]= data list'
                    if modNum <=3:
                        while modNum >0:
                            str = str.join(['',item[1][0]])#concatenate the Roman character each time
                            modNum -=1
                    elif modNum <5:
                        str = item[1][1]
                    elif modNum ==5:
                        str = item[1][2]
                    elif modNum < 9:
                        str = item[1][2] # catch the base of the 'five'
                        while modNum > 5:
                            str = str.join(['',item[1][0]])# concatenate the 'five' with the rest of 'ones'
                            modNum -=1
                    else:
                        str = item[1][3]
                else:
                    while modNum > 0: #check for the 'thousands'
                        str =str.join(['',item[1][0]])
                        modNum -=1
                retstr = str.join(['',retstr])
        return retstr
                        
                
                
                
