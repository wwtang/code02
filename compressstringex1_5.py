"""implement a method to compress a string with repeats

ex: aabccccaaa would become a2bc4a3

if the "compressed" string would not be shorted than the original string, then return the original string


algorithm:
1. initialize result = [], and checkedIndex  =[],count = 1
2. scane the string with index i and j ,where j = i+1.
3, while string[i] == string[j], count +=1, j +=1
4. update the result, checkedIndex, and count
5. Before begin the next while loop, check if the i larger than element in the checkedIndex, if yes, begin
the while loop, else, goes to next i

"""
def compressStr(string):
    if len(string) <2:
        return string
    result = []
    checkedI= [0]
 
    
    for i in range(len(string)-1):
        count = 1
        j = i +1
        if i >= checkedI[-1]:
           
            while j <= len(string) - 1 and string[i] == string[j]:
                count +=1
                j +=1
                
            checkedI.append(j)
            result.append(string[i] + str(count))

    print "length of result %s and string %s"%(len(result), len(string))
            
    if len(result) >= len(string):
        return string
  
    return "".join(result)

def main():
    strings = ["aabccccaaa","asdf", 'aaaaaa',"ab"]
    
    print [compressStr(string) for string in strings]

if __name__=="__main__":
    main()
        
    
