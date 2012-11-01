"""
max_heapfy: compare the parent node and its left and right son, set the largest at the parent and do recursive at the largets index
build heap: begin from the (n/2) backto 0, max_heapfy
heap sort
"""

def max_heapfy(lst,i):
    #node starts from index 0 
    l = 2*i+1
    r = 2*i+2
    n = len(lst)-1
    if l <=n and lst[l] > lst[i]:
        largest = l
    else:
        largest = i

    if r <=n and lst[r] >lst[largest]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapfy(lst, largest)
        
# first, last is very efficient
def max_heapfy1(lst, first, last):
    left =  2*first +1
    right = 2*first +2
    if left <= last and lst[left] >lst[first]:
        largest = left
    else:
        largest = first

    if right <= last and lst[right] > lst[largest]:
        largest = right
    if largest != first:
        
        lst[first], lst[largest] = lst[largest], lst[first]
        
        max_heapfy1(lst, largest, last)
        

def build_heap(lst,first,last):
    i = last/2
    while i >=first:
        
        max_heapfy(lst,i)
        
        i -= 1
    return lst

def create_heap(lst, first, last):
    for i in range(last/2, 0 , -1):
        max_heapfy(lst, first)
    return lst
        

def create_heap1(lst, first, last):
    for i in range(last/2, 0 , -1):
        max_heapfy1(lst, first, last)
    return lst


def heap_sort(lst):
    first = 0
    last = len(lst)-1
    create_heap(lst, first, last)
    for i in range(last, first, -1):
        lst[i], lst[first] = lst[first], lst[i]
        max_heapfy1(lst, first, i-1)
    return lst


def establish_heap_property(list2, first, last):
 #   left = 2*first +1#
    while 2 * first + 1 <= last:
        k = 2 * first + 1# assume the lef child is the largest 
        if k < last and list2[k] < list2[k + 1]:# compare the left and right son, find the larger one
            k += 1
        if list2[first] >= list2[k]:# if parent is the largest, break
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap, swap the parent with the largest son
        first = k # next is the largest son
    
def main():
    lst = [16,4,10,14,7,9,3,2,8,1]
    print"build heap: ", build_heap(lst,0,len(lst)-1)
    print "create_heap: ", create_heap(lst,0,len(lst)-1)
    print "create_heap1: ", create_heap1(lst,0,len(lst)-1)
    print "sort:",  heap_sort(lst)



if __name__=="__main__":
    main()
    
