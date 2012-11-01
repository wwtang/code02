""" qitang"""

#count_sort, assumes that each of the n input element are integers and in range 0 to k

def count_sort(lst,k):
    #initialize a auxiliary array counter
    counter = [0]*(k+1)

    #index of counter is the value of lst, value of counter is the amount of element in the lst	
    for value in lst:
        counter[value] +=1
	
    #arr is  the output array
    arr = []
    for value, amount in enumerate(counter):
        arr.extend([value]*amount)
    return arr

def count_sort1(lst,k):
    #initialize the auxiliary array
    counter = [0]*(k+1)

    #counter[i] contains the amount of element that equals i
    for value in lst:
        counter[value] +=1
    print counter

    #now counter[i] contains the amount of element that equals or less than i
    #for value in counter : not the value
    for i in xrange(1, k+1):
        counter[i]  += counter[i -1]
    print counter

    #output array
    # arr should be assigned with length, because it used as index, not append or extend
    arr = [0]*len(lst)
    for i in xrange(len(lst)-1, -1, -1):
        arr[counter[lst[i]]-1] = lst[i]#counter[lst[i]] is the final position of element lst[i] in output array arr
        counter[lst[i]] -= 1# move forward the final position of lst[i] by 1
    return arr

def main():
    lst = [2,5,3,0,2,3,0,3]
    print "count_sort: ", count_sort(lst,5)
    print "count_sort1: ", count_sort1(lst,5)

if __name__=="__main__":
    main()
    
		
