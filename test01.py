"""
remove "n" from "next" and return "ext"
if "n" not in "ext" return CharacterNotFound
"""
#arr is the target string, x is the character will be removed
def RemoveChar(arr, x):
    n = len(arr)
    result = list(arr)
    for index, elem in enumerate(result):
        if elem == x:
            result.pop(index)
                
    if len(result) == n:
        
        print "Character %s is not in the target string %s" %(x,arr)
        raise Exception, "CharacterNotFound"
        
                
    
    return "".join(result)    
def main():
     arr = "solution"
     print RemoveChar(arr,"o")
     arr1 = "exception"
     RemoveChar(arr1,"y")
 
if __name__=="__main__":
    main()
