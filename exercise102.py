"""
exercise10.3
1. find the rotated point
2 apply binary search to the left and  right side of rotated point
"""
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
    
def search_rotated_array(arr, x):
    n = len(arr)
    rp = 0
    if len(arr) < 2:
        return arr
    for i in range(n):
        if arr[i-1] >arr[ i]:
            rp = i-1
    if arr[rp] == x:
        return arr[rp]
    if x > arr[rp] or x <arr[rp+1]:
        print "x is not in this array"
    if x > arr[0]:
        return binary_searchR(arr, 0 , rp-1,x)
    if x< arr[n-1]:
        return binary_searchR(arr, rp+1,n-1,x )

def main():
    arr= [15,16,19,20,25,1,3,4,5,7,10,14]

    print search_rotated_array(arr, 10)
    print search_rotated_array(arr, 5)
    print search_rotated_array(arr, 7)


    

if __name__=="__main__":
    main()
