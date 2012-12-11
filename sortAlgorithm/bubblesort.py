""""""

import random
import time

DEBUG = False

N  = 1000
list1 = []

for i in range(0,N):
    list1.append(random.randint(i, N-1))# produce a random int number in (0, N)

#we can apply decorator to all the functions to print uniform format 
def print_time(func):#caculate the run time of func decorate the wrapper function
    def wrapper(*argv):
        t1 = time.clock()
        res = func(*argv)
        t2 = time.clock()
        print "%s took %0.3fms"%(func.func_name,(t2-t1)*1000.0)
        return res
    return wrapper

def print10(list2):
    for k in range(10):
        print list2[k]
    print
    
@print_time
def bubble_sort(list2):
    for i in range(0, len(list2)-1):#in the I+ loop just check the list2[:-i] element, due to the last elment is the largest
        swap_test = False # swap tag
        for j in range(0, len(list2) - i -1):#move the larges element to the end in one loop, 
            if list2[j] > list2[j+1]:#compare the adjacent two element
                list2[j], list2[j+1] = list2[j], list2[j+1]
                sawp_test = True# toggle the flag
        if swap_test  == False:#no swap did in the loop
            break

# set the first element as the min, then compare the min with the rest, find the min and swap it wih the firt
@print_time
def selection_sort(list2):
    for i in range(0, len(list2)):
        min_index = i# set the first element as min
        for j in range(i+1, len(list2)):#traversal the rest to find the really min value
            if list2[j] < list2[min_index]:
                min_index = j
        list2[i],list2[min_index] = list2[min_index], list2[i]# swap 
    

@print_time
def insert_sort(list2):#compare the current element with its prior element, if smaller, insert it at the left of them
    for i in range(1,len(list2)):#begin from the second element
        save = list2[i] # save the current elem, use to compare with its prior elements
        j = i# j here used as helper index
        while j >0 and  list2[j-1] > save:# chek the the current element with all the prior elements one by one
            list2[j] = list2[j-1]# 
            j -=1#backloop to the beginng
        list2[j] = save#here j is located at the corret postition, after while loop



#write like this because we want to use the print_time decorator
@print_time
def qsort(list2):
    return quicksort(list2)


def quicksort(list2):
    if len(list2)<2:
        return list2
    pivot = random.choice(list2)
    lessor = [i for i in list2 if i< pivot]
    greater = [i for i in list2 if i > pivot]
    return quicksort(lessor) + [pivot] +quicksort(greater)

@print_time
def mergesort1(list2):
    return mergesort(list2)

def mergesort(list2):
    if len(list2)<=1:
        return list2
    left = mergesort(list2[:len(list2)/2])
    right = mergesort(list2[len(list2)/2 :])
    result = []
    while len(left) >0 and len(right)>0:
        if left[0] > right[0]:
            result.append(right.pop(0))#pop delete the first element function like flag -=1
        else:
            result.append(left.pop(0))
    if (len(left)>0): result.extend(mergesort(left))
    else: result.extend(mergesort(right))
    return result


@print_time
def mergesort2(list2):
    return mergesort02(list2)

def mergesort02(list2):
    if len(list2) <= 1:
        return list2

    left = mergesort02(list2[: len(list2)/2])
    right = mergesort02(list2[len(list2)/2 :])

   #partition part
    i = j = 0
    result = []
    while len(result) < len(right)+len(left):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
        if i==len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result
        
    
if __name__ == "__main__":
    list2 = list(list1)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    bubble_sort(list2)

    if DEBUG:
        print10(list2)
    list2 = list(list1)
    selection_sort(list2)
    
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    
    insert_sort(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    qsort(list2)

    if DEBUG:
        print10(list2)
    list2 = list(list1)
    mergesort1(list2)
    if DEBUG:
        print10(list2)
    list2 = list(list1)
    mergesort2(list2)
