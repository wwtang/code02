"""radixbucket sort

sort the element range from 100 to 999
initalize buckets
distribute buckets
(sorted each bucket) use radix sort
concatecate each bucket together

"""

import time
def sort_time(func):
    def wrapper(*arg):
        t1 = time.clock()
        res = func(*arg)
        t2 = time.clock()
        print "%s took %0.3f ms "%(func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper
        



@sort_time
def radix_bucket(array):

    length = len(str(array[0]))# element of array are int numbers
    buckets = [[] for i in range(0,10)]#0...9

    #begin from the least important digit
    for digit in range(length, -1,-1):
        for number in array:
            buckets[number/10**(length - digit)%10].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array

@sort_time
def merge_sort1(array):
    return merge_sort(array)

def merge_sort(array):
    #the most basic operation when element are splited
    #the core is: when length of list is one, begin to sort
    if len(array)<2:
        return array
    
    mid = len(array)/2
    left = merge_sort(array[ : mid])# contains the element right before mid
    right = merge_sort(array[mid : ])#contains elements start from mid
    return mergesq(left, right)
 

def mergesq(sq1,sq2):#sq1 and sq2 are sorted, except when they contain only one element
    result = []
    while sq1 and sq2:
        if sq1[0] <= sq2[0]:
            result.append(sq1.pop(0))
        else:
            result.append(sq2.pop(0))       
    result.extend(sq1 or sq2)
    return result

@sort_time
def quick_sort1(array):
    return quick_sort(array)
def quick_sort(array):
    
    if len(array) < 2:
        return array
    
    mid = len(array)/2
    pivot = array[mid]
    lesser = [x for x in array if x <pivot]
    greater = [x for x in array if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


@sort_time
def bubble_sort(array):
    if len(array) <2:
        return array
    swapped = True
    while swapped:
        swapped =False
        for i in range(len(array)-1):# if range(len(array)), the j +1 will exceed the range 
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    return array


def bubble_sort1(array):
    if len(array) < 2:
        return array
    n = len(array)
    
    for i in xrange(0,n):
        for j in xrange(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

@sort_time
def insert_sort(array):
    if len(array) < 2:
        return array
    n = len(array)
    for i in range(0,n):
        tmp = array[i]
        j = i
        while j >0 and array[j-1] > tmp:#prior element larger than the current element
            array[j] = array[j-1]#move the j-1 to j
            j -=1
        array[j] = tmp#insert the tmp at the corret postion
    return array

@sort_time
def select_sort(array):
    if len(array) <2:
        return array
    minindex = 0
    n = len(array)
    for i in range(1,n):
        if array[i] < array[minindex]:
            array[i], array[minindex] = array[minindex], array[i]
            minindex = i
    return array

#used for heap sort
def max_heapfy(array, k, last):
    left = 2*k +1
    right = 2*k +2

    if left<= last and array[left] > array[k]:
        largest = left
    else: largest = k

    if right <=last and array[right] > array[largest]:
        largest = right
    if largest != k:
        array[largest], array[k] = array[k], array[largest]
        max_heapfy(array, largest, last)
 

def build_heap(array):
    last = len(array)-1
    n = last/2
    for i in range(n, -1,-1):
        max_heapfy(array, i, last)
 
@sort_time       
def heap_sort(array):
    last = len(array) -1

    build_heap(array)

    for i in range(last, -1, -1):
        array[0], array[i] = array[i], array[0] # swap the first with last element,
        max_heapfy(array, 0, i-1)# now reduce the heapfy size by 1
    return array
 
@sort_time
def normal_sort(array):
    return sorted(array)
                
def main():
    import random
    array = [random.randint(100,999) for i in range(1000)]
    #print array
    #print "sorted_array:  ", sorted(array)
    #print "radix_bucket: ", radix_bucket(array)
    #print "merge_sort:    ", merge_sort(array)
    #print "quick_sort:     ", quick_sort(array)
    #print "heap_sort:      ", heap_sort(array)
    #print "insert_sort:     ", insert_sort(array)
    #print "select_sort:     ", select_sort(array)
    print "timing 7 sorting algorithm"
    normal_sort(array)
    radix_bucket(array)
    heap_sort(array)
    merge_sort1(array)
    quick_sort1(array)
    bubble_sort(array)
    insert_sort(array)
    select_sort(array)
 
 
    print "***********"
    print "***********"
    arr = [random.randint(0,999) for i in range(1000)]
    normal_sort(arr)
    heap_sort(arr)
    merge_sort1(arr)
    quick_sort1(arr)
    bubble_sort(arr)
    insert_sort(arr)
    select_sort(arr)
 
    
if __name__=="__main__":
    main()

    
