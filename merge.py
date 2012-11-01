""" merge sort """


import random
import time

N = 20
list1 = []


for i in range(0, N):
    list1.append(random.randint(0,N-1))

def merge_sort(list2):
    merge_sort_r(list2, 0, len(list2) - 1)
    
def merge_sort_r(list2, first, last):
    if first <last:
        sred = (first+last)/2
        merge_sort_r(list2, first, sred)
        merge_sort_r(list2, sred+1, last)

        merge(list2, first, last, sred)


def merge(list2, first, last, sred):
    helper_list = []
    i = first# the first num in the left part
    j = sred+1# first num in the right part

    while i <= sred and j<= last:# left ,right parts is not empty
        if list2[i] <= list2[j]:
            helper_list.append(list2[i])#remove the element to helper_list
            i += 1#move to right
        else:
            helper_list.append(list2[j])
            j += 1# move to right

    while i <= sred:# right part is empty, add all the rest element of the left part to the helper_list
        helper_list.append(list2[i])
        i +=1

    while j<=last:#left is empty, add all the rest element of the right part to helper_list
        helper_list.append(list2[j])
        j +=1

    for k in range(0, last - first +1):
        list2[first + k] = helper_list[k]


if __name__=="__main__":
    list2 = list(list1)
    print list2
    merge_sort(list2)
    print list2
    
