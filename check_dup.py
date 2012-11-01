#check the dupliacte element of a list and return True if duplicate

def check_dup(l):
        unique_l = list(set(l))
        print unique_l
        print len(unique_l)
        if len(l) != len(unique_l):
            return True
        print l
 
        
            
