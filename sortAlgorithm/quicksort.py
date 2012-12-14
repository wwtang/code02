""" quicksort in python
tree parts
1, recursive apply quicksort to the divide parts of the original arry
2, use the "Partition " function to return the  pivot
3, swape the value
left,right are index not  the value
"""

def quicksort(array, left, right):
    if len(array) == 0 or len(array) == 1:
        return array

    if left < right:
        index = partition(array,0,len(array)-1)
        print index,"index"
        quicksort(array, left, index-1)
        quicksort(array,index+1,right)


def partition(array, p,r ):
    x = array[r]
    i  =  -1
    for j in range(len(array)-2):
        if array[j] <= x:
            i += 1
            #swape the array[i] and array[j]
            array[i],array[j] = array[j],array[i]

    array[i+1], x = x, array[i+1]
    return array[i+1]


def test(got, expect):
    if got == expect:
        print "OK"
    else:
        print "No"
        print "got : ", got, "expect: ", expect

def main():
    print "***"
    test(quicksort([1,3,6,2],[1,2,3,6])

if __name__=="__main__":
    main()