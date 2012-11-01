""" ex10.5
Question: Given a sorted array of string which is interspersed with empty string.
Write a method to find the location of a given string

**************
The common way to find a stirng is to use binary search, while this array is interspersed, we need to
modfiy the bianry search condition to apply this algorithm to the array.
So what's the problem here is how to find the middlest non-empty string?

How to find the exact mid non- empty string?
Goes from the mid  = (first+last)/2
if mid is empty, goes to the right and left side to find the first non-empty stirng, make it as the mid string.
Then apply the regular bianry search on the array to get our answer.

example:

input:  find "ball" in {"at", "","","","ball", "","","car", "","","dad","",""}
output :4

"""

def find_mid(arr, first, last):

    mid = (first + last)/2

    # left and right shoud be initialized first, otherwise there will be anboundLocalError: local variable 'left' referenced before assignment
    left =right= 0
  
    
     #find the mid
    if len(arr[mid]) == 0:
        left = mid - 1
        right = mid +1

    while True:
        if left < first and right >last:# rember the limitation
            return None
        if left >= first and len(arr[left]) != 0:# cao ni ma, you wang le ">=" suo yi zhao bu dao diyige 
            mid = left
            break
        elif right <= last and len(arr[right] )!= 0:
            mid = right
            break
        left -=1
        right +=1
    return mid

def find_interspersed(arr, first, last, string):
    
    if len(arr) < 1 or  len(string) == 0 :
        return None
    
    # check if mid is empty
    mid = (first+last)/2
    # if arr[mid]  is Null,call find_mid function to find the non-empty string
    if len(arr[mid]) == 0:
        mid = find_mid(arr, first, last)

    if arr[mid] == string:
        return mid
    
    if arr[mid] > string:#search left
        return find_interspersed(arr, first, mid-1, string)
    if arr[mid] < string:#search right
        return find_interspersed(arr, mid+1, last, string)
    
    


def main():
    arr = ["at", "","","","ball", "","","car", "","","dad","",""]
    print find_interspersed(arr, 0, len(arr)-1, "at")
    print find_interspersed(arr, 0, len(arr)-1, "ball")
    print find_interspersed(arr, 0, len(arr)-1, "car")
    print find_interspersed(arr, 0, len(arr)-1, "dad")
    
if __name__=="__main__":
    main()







    

   
