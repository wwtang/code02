"""sort"""
import random
#merge_sort, recursively merge_sort its left and right side

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

def quick_sort(array):
    
    if len(array) < 2:
        return array
    
    mid = len(array)/2
    pivot = array[mid]
    lesser = [x for x in array if x <pivot]
    greater = [x for x in array if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


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

def insert_sort(array):
    if len(array) < 2:
        return array
    n = len(array)
    for i in range(1,n):
        tmp = array[i]
        j = i
        while j > 0 and array[j] > tmp:
            array[j] = array[j-1]#move the j-1 to j
            j -=1
        array[j] = tmp#insert the tmp at the corret postion
    return array

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
def min_heapfy(array, k):
    n = len(array)
    if k < n/2:
        l = 2*k +1
        r = 2*k +2
        smallest = k
        if array[l] < array[smallest]:
            smallest = l
        elif array[r] < array[smallest]:
            smallest = r
        if smallest != k:
            min_heapfy(array, smallest)

def build_heap(array):
    n = len(array)
    for i in range(n/2, -1, -1):#begin from the last parent
        min_heapfy(array, i)
    return array
        
def heap_sort(array):
    n = len(array)
    array = build_heap(array)
    i = 0
    while i < n:
        array[0], array[-1] = array[-1], array[0]
        min_heapfy(array, 0)
        i +=1
    return result

    
                
        

def main():
    array = [random.randint(0,100) for i in range(20)]
    print "merge_sort:"
    print merge_sort(array)
    print "quick_sort: "
    print quick_sort(array)
    print "bubble_sort: "
    print bubble_sort1(array)
    print "insert_sort: "
    print insert_sort(array)
    print "select_sort: "
    print select_sort(array)
    print "heap_sort: "
    print heap_sort(array)

if __name__=="__main__":
    main()
        
