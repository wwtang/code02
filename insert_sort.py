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
        max_heapfy(array, largest, last)
 

def build_heap(array):
    last = len(array)-1
    n = last/2
    for i in range(n, 0,-1):
        max_heapfy(array, i, last)
 
        
def heap_sort(array):
    last = len(array) -1

    build_heap(array)

    for i in range(last, -1, -1):
        array[0], array[i] = array[i], array[0] # swap the first with last element,
        max_heapfy(array, 0, i-1)# now reduce the heapfy size by 1
    return array

                
def main():
    import random
    array = [random.randint(100,999) for i in range(8)]
    print array
    print "sorted_array:  ", sorted(array)
 
    print "heap_sort: \n", heap_sort(array)
 

if __name__=="__main__":
    main()
