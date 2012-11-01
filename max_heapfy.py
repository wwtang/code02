"""max heapfy"""

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

def build_heap(lst):
    n =len(lst)
    #[5,4,3,2,1] no 0
    for i in range(n/2, 0,-1):
        max_heapfy(lst,i-1)
    return lst

#def heap_sort(lst)


def create_heap(lst):
    first = 0
    last =len(lst)-1
    i = last /2
    while i >= first:
        max_heapfy(lst, i)
        i -=1
    return lst

def heapsort(lst):
    first = 0
    last = len(lst)-1
    create_heap(lst)
    for i in range(last, first, -1):
        lst[i], lst[first] = lst[first],lst[i]
        lst = lst[:-1]
        max_heapfy(lst,0)


def main():
    lst = [16,4,10,14,7,9,3,2,8,1]
    print   build_heap(lst)
    print create_heap(lst)
    print heapsort(lst)
    
if __name__== "__main__":
    main()
