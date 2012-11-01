"""
remove the duplicates from input string
"""

def removeDup(string):
    sortedstr = sorted(string)
    
    #popi = []
    #i = 1
    #for i in range(1,len(sortedstr)-1):
    #while i <= len(sortedstr)-1:
    #    print sortedstr, len(sortedstr)

    #    if sortedstr[i] == sortedstr[i-1]:
    #        popi.append(i-1)
    #        #sortedstr.pop(i-1)

    #    i +=1
    #print popi
    #for i in popi:
    #    print i
    #    sortedstr.pop(i)
    #print popi
    #return "".join(sortedstr)

    



def main():
    #string ="elements"
    #print removeDup(string)
    string = "eeeee"
    print removeDup(string)

if __name__=="__main__":
    main()
