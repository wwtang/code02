def insert_sort(list2):#compare the current element with its prior element, if smaller, insert it at the left of them
    for i in range(1,len(list2)):#begin from the second element
        save = list2[i] # save the current elem, use to compare with its prior elements
        j = i# j here used as helper index
        while j >0 and  list2[j-1] > save:# chek the the current element with all the prior elements one by one
            list2[j] = list2[j-1]# 
            j -=1#backloop to the beginng
        list2[j] = save#here j is the 0, the result of while loop
    return list2



list2 = [3, 7,4, 9, 5, 2, 6, 1]
if __name__=="__main__":
    print insert_sort(list2)
