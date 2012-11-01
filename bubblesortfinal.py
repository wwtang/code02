""" bubble sort, compare the adjacent two elemnets, through every loop the last element is the largest
so, there is no need to check the last element,
the tag of finishing sorting is that no sawp exists in the loop

"""
# no check for the sorted largest element at last, 
def bubblesort1(lst):
    if len(lst) <= 1:
        return lst
    for passleft in range(len(lst)-1, 0, -1):#0-7/0-6....
        for i in range(0, passleft):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

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

def test(got, expected):
    if got == expected:
        print "OK"
    else:
        print "X"
        print "got: ", got, "expected: ", expected

def main():
    lst = [32,21,2,7,56,75,4,17,1]
    sortedlst = sorted(lst)
    test(bubblesort1(lst), sortedlst)
    test(bubblesort2(lst), sortedlst)
    test(bubblesort3(lst), sortedlst)


if __name__=="__main__":
    main()
