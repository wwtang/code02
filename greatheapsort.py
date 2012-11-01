"""great heap sort
functions used in heap sort:
max_heapfy
build a heap
heap is a array, the essential algorithm here is the realtion between different elements

"""

def max_heapfy(array, k, last):#heapfy works among three elenment
    left = 2*k +1
    right = 2*k +2

    # find the largest element in the unit heap
    if left <=last and array[left] > array[k]:
        largest = left
    else:
        largest = k

    if right <= last and array[right] > array[largest]:
        largest = right
    if largest !=k:
        array[largest], array[k] = array[k], array[largest]
        max_heapfy(array, largest, last)
        

def build_heap(array, last):
    n = last/2
    for i in range(n, -1, -1):
        max_heapfy(array, i, last)
    return array

def heap_sort(array):
    first = 0
    last = len(array) -1
    build_heap(array, last)
    print "heap: ", array
    #for i in range(0, last):
    for i in range(last, -1,-1):#swap from the end of the array, the end is the largest, i is the last
        array[first], array[i] = array[i], array[first]
        
        max_heapfy(array, first, i-1)# i-1 is the last element in the array that needs to be heapfied
    return array
    
    
def main():
    lst = [16,4,10,14,7,9,3,2,8,1]
    #print"build heap: ", build_heap(lst,0,len(lst)-1)
    #print "create_heap: ", create_heap(lst,0,len(lst)-1)
    #print "create_heap1: ", create_heap1(lst,0,len(lst)-1)
    print "sort:",  heap_sort(lst)



if __name__=="__main__":
    main()
