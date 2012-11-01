
def light_on(n):
    light = [0]*n
    for pas in range (1,n+1):
        for index in range(pas,n+1):
            
            if index % pas == 0:
                light[index-1] +=1
    result = [i for i in light if i%2==1]
    

    return len(result)
    
