"""test"""

def heap_sort(list2):
    first = 0
    last = len(list2) -1

    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]
        establish_heap_property(list2, first, i-1)



def create_heap(list2, first, last):
    i = last/2# index of the the last leaf node's parent
    while i >=first:#
        establish_heap_property(list2, i, last)
        i -=1

def establish_heap_property(list2, first, last):
    while 2*first +1 <=last:# odd number
        k = 2*first +1#k is the right son of the "first"  node

        if k < last and list2[k] < list2[k+1]:
            k +=1
        if list2[first] >= list2[k]:# parent larger than son, fit the heap condition , break
            break

        list2[first], list2[k] = list2[k], list2[first]# swap the son and parent
        first = k
