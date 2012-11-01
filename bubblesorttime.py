"""compare the run time of different methods"""
import time
import random

N = 1000
lst = []
for i in range(N):
    lst.append(random.randint(0, N-1))
    
def print_time(func):
    def wrapper(*argv):
        t1 = time.clock()
        res = func(*argv)
        t2 = time.clock()
        print  "%s took %0.3f ms" % (func.func_name, (t2-t1)*1000.00)
        return res
    return wrapper

@print_time       
# no check for the sorted largest element at last, 
def bubblesort1(lst):
    if len(lst) <= 1:
        return lst
    for passleft in range(len(lst)-1, 0, -1):#0-7/0-6....
        for i in range(0, passleft):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

@print_time
# This method checks the well sorted largest elements, and this is no necessary,
def bubblesort2(lst):
    if len(lst) <= 1:
        return lst
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]
                swapped = True#check the entir list every time, until there is no swapping happens
    return lst

@print_time
#associated the above tow methods together, just check the unsorted elements and set swap tag
def bubblesort3(lst):
    if len(lst) <= 1:
        return lst
    swapped = False
    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if swapped == False:
            break
    return lst


if __name__=="__main__":
    lst = list(lst)

    print "see below"
    bubblesort3(lst)
    bubblesort2(lst)
    bubblesort1(lst)
    
    bubblesort3(lst)
    bubblesort2(lst)
    bubblesort1(lst)
   



    

