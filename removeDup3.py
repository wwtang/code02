"""remove duplicate characters of input string



"""


def removeDup3(string):
    if len(string) <2:
        return string

    i = 1
 
    n = len(string)
    sortedstr = sorted(string)
    result = [sortedstr[0]]


    while i <=n-1:
        if sortedstr[i] !=sortedstr[i-1]:
            result.append(sortedstr[i])

        i +=1
    return "".join(result)

def main():
    strings = ["geeksofgeeks","aa",' ', 'gekof']
    
    print [removeDup3(string) for string in strings]

if __name__=="__main__":
    main()
            
            
