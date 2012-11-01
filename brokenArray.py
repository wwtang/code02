"""
Good = [10,20,30,40,50,80,100,110,120]
 
Broken = [100,110,120, 10,20,30,40,50,80]

search the broken array to find the target element and return its index
x in the target element
arr is the broken array
test for both good and broken array

"""


def searchBroken(arr,left,right, x):
    #invalid index
    if right < left:
        return None
    #mid
    mid = (left+right)/2
    if arr[mid] == x:
        return mid

    #determine the ordered part of the arry according to arr[left] and arr[mid]
    #left part is well ordered
    if arr[left] <= arr[mid]:
        
        if  arr[left] <=x<=arr[mid]:            
            return searchBroken(arr,left, mid-1, x)
        else:
            return searchBroken(arr,mid+1,right, x)
    
    #right part is well ordered      
    if arr[left] >= arr[mid]:
        if arr[mid] <= x <arr[left]: # no "=" on the right side             
                return searchBroken(arr, mid+1,right, x)
        else:              
                return searchBroken(arr,left, mid-1, x)

        
def test(got, expect):
    if got == expect:
        print "OK"
    else:
        print "got: " + str(got) + " , expect: " + str(expect)
        
def main():
    print"test for borken array"
    #broken array
    broken = [100,110,120, 10,20,30,40,50,80]
    left = 0
    right = len(broken)-1
    test(searchBroken(broken, left, right,100), 0)
    test(searchBroken(broken, left, right,110), 1)
    test(searchBroken(broken, left, right,120) ,2)
    test(searchBroken(broken, left, right,10), 3)
    test(searchBroken(broken, left, right,20), 4)
    test(searchBroken(broken, left, right,30), 5)
    test(searchBroken(broken, left, right,40), 6)
    test(searchBroken(broken, left, right,50), 7)
    test(searchBroken(broken, left, right,80), 8)

    print"Test for good array"
    #good array
    Good = [10,20,30,40,50,80,100,110,120]
    left = 0
    right = len(Good)-1
    test(searchBroken(Good, left, right,10), 0)
    test(searchBroken(Good, left, right,20), 1)
    test(searchBroken(Good, left, right,30), 2)
    test(searchBroken(Good, left, right,40), 3)
    test(searchBroken(Good, left, right,50), 4)
    test(searchBroken(Good, left, right,80), 5)
    test(searchBroken(Good, left, right,100), 6)
    test(searchBroken(Good, left, right,110), 7)
    test(searchBroken(Good, left, right,120), 8)
    
if __name__=="__main__":
    main()
