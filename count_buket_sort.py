""" count_sort and buket sort """


def count_sort(lst, k):#k is the range of the input element, and k should be less than the lenth of lst
    #create a auxiliary list: counter
    counter = [0]*(k+1)
    for value in lst:
        counter[value] += 1

    #rearrange the element according to the information of counter
    arr = []
    for value, amount in enumerate(counter):
        arr.extend([value]*amount)
    return arr


def bucket_sort(lst):
    #similar to count sort, except that the input element are assumed to be uniformly distribute, so there is nok
    counter = [0]*len(lst)
    #create the counter
    for value in lst:
        counter[value] +=1
    #rearrange the lst according to the distribution
    arr= []
    for value, amount in enumerate(counter):
        arr.extend([value]*amount)
    return arr
        


def main():
    lst = [2,5,3,0,2,3,0,3]
    print  count_sort(lst,5)
    lst1= [78,1,7,39,26,72,94,21,12,23,68]
    
if __name__=="__main__":
    main()
