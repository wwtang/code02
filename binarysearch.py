"""binary search"""

#arr is the target search arrary sv is the query value
def binary_search(arr, sv):

    low = 0
    hight = len(arr) - 1
 

    while low < hight:
        mid  = (low+hight)/2
        if sv == arr[mid]:
            return mid
        elif sv > arr[mid]:
            low = mid+1
        else:
            hight = mid - 1
    
    print "%s is not in this array" % sv
    return None


def binary_searchR(arr, low, high, sv):
    if low > high:
        return None
    mid = (low+high)/2
    if sv == arr[mid]:
        return mid
    elif sv > arr[mid]:
         return  binary_searchR(arr, mid+1,high ,sv)
    else:
        return    binary_searchR(arr, low, mid ,sv)



    
def main():
 #   arr = range(10)
    arr = [11,22,33,44,55,66]
    print   binary_search(arr, 11)
    print   binary_search(arr, 33)
    print   binary_search(arr, 333)
    print "*******************"
    print   binary_searchR(arr,0, 5,11)
    print   binary_searchR(arr, 0,5, 22)
    print   binary_searchR(arr, 0,5, 33)
    print   binary_searchR(arr, 0,5, 55)

    
    print   binary_searchR(arr, 0,5,333)


if __name__=="__main__":
    main()
    
            
