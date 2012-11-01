"""
ex10.3
Question: Given a sorted array that has been rotated an unknown number of times, give an a(lgn) algorithm
that find and element in the array. You may assume that the array was origninally sorted in increaseing order

*****************************
You first algorithm was to find the largest element of the array, and then apply binary search to the right and
left side of the largest point. However, to find the max elemnet costs 0(n), which is not fit the requirement
totally wrong!!!

So, o(lgn) means the binary search.  what's the difference is the application area. The key point is how to
divide the array so that we can apply binary search

Rotated array means at leasst one half of the array is well ordered(increase order).

if arr[left] < arr[mid] : the left part is ordered      (ex{10,15,20,0,5})
if arr[left] > arr[mid] : the right part is ordered    (ex{50,5,20,0,40})
if arr[left] == arr[mid]:{#
                                    if arr[left] != arr[right] the left part is all repeats: {2,2,2,3,4} or{2,2,2,0,1}
                                    if arr[left] = arr[mid] = arr[right]: need to check the both two half
                                    {2,2,2,1,2}or{2,1,2,2,2}


                                    }
"""

def searchBroken(arr,left,right, x):
 #   left = 0
 #   right = len(arr)-1
    mid = (left+right)/2
    if arr[mid] == x:
        return mid

    
    if  right < left:# endless loop, check the extreme condition
        return None

    if arr[left] < arr[mid]:#left side if well ordered
        if arr[mid] > x and arr[left] > x: # !!!!!write the correct limitation condition
            return searchBroken(arr,mid+1,right, x)#search right
        else:
            return searchBroken(arr,left, mid-1, x)#search left
            
    if arr[left] > arr[mid]:
        if arr[mid] > x and arr[left] > x:
            return searchBroken(arr,left, mid-1, x)#search left
        else:
            return searchBroken(arr, mid+1,right, x)#search right

    if arr[left] == arr[mid]:
        if arr[left] != arr[right]:# left are repeats
            return searchBroken(arr,mid+1,right, x)
        
        elif arr[left] == arr[right]:#search both the left and right. Remeber
            result = searchBroken(arr,left,mid-1, x)#search left
            
            if result is None:
                return  searchBroken(arr,mid+1,right, x)#search right
            else:
                return result 
        return None# this None belong to result



def main():
    arr1 = [10, 15,20,0,5]
    arr2 = [50,5,20,30,40]
    arr = [2,2,2,3,5]
    arr3 = [ 2, 2, 2, 5, 2]
    arr4 = [2,5,2,2,2]

    left = 0
    right = len(arr1)-1

    print searchBroken(arr1, left, right,10)
    print searchBroken(arr2, left,right, 30)
    print searchBroken(arr, left,right, 3)
    print searchBroken(arr3 ,left,right,2)
    print searchBroken(arr4, left,right, 2)

if __name__=="__main__":
    main()





    

    













            

    
