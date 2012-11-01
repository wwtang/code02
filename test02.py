"""
create a dict, 
set the element of the list as key
set its frequency as value
return the list of duplicated element
"""

def findDuplicate(lst):
    if len(lst) < 2:
        return None
    result = {}
    for elem in lst:
        if elem not in result:
            result[elem] = 1
        else: result[elem] +=1
	
    duplst = []
    for k,v in result.items():
        if v >1:
            duplst.append(k)
    return duplst

def test(got, expected):
    if got == expected:
        print "OK"
    else:
        print "NO", "got", got, " but expected ", expected
		
def main():

    lst = [1,3,2,4,1,1,4]
    test(findDuplicate(lst), [1,4])
    
    lst1 = [1,2,3,4,5]
    test (findDuplicate(lst1),[])

    lst2 = [1,2,3,4,2,3]
    test(findDuplicate(lst2),[2,3])
    lst3 = []
    test(findDuplicate(lst3),[])
	
if __name__=="__main__":
    main()	

		
