# the traditional method to remove the duplicated element of string

def removeDup1(raw_str):
    #check the size of raw_str
    if raw_str == '':
        print 'The string is empty'
        return
    if len(raw_str) <2:
        print 'There is only one character in the string'
        return

    new_str = []#used for storing unique characters
    dup_ele = []#used for storing duplicated characters
    for c in raw_str:
        if c not in new_str:
            new_str.append(c)
        else:
            dup_ele.append(c)
    if len(dup_ele) != 0:
        print "The duplicate character in the raw_string is: " + ' '.join(dup_ele)
        
def removeDup2(raw_str2): # This method will find the first duplicate character
    #Check the lenth of the input string
    if len(raw_str2) <=1:
        print 'The string is empty or only one character'
        return
    else:
        i = 1
        raw_str = ''
        raw_list = list(raw_str2)
        for c in raw_list:
            if c not in raw_list[ i: ]:
                print c
                print raw_list[i:]
                i +=1
            else:
                raw_list = raw_list.remove(c)
        raw_str = ''.join(raw_list)
        print raw_str
        return

def removeDup3(raw_str3):
    if len(raw_str3) <=1:
        print 'The string is empy or only have one character'
    else:
        if len(raw_str3) != len(set(raw_str3)):
            print "The string has duplicated characters"
        else:
            print "All the characters are unique in this string"
            
    
 
                
            
            
            
        
    
