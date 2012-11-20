"""
search the rotated array and find the target, integer in array not be not distinguished 

"""

def search(arr,x,lindex,rindex):
	if len(arr) <2:
		return arr

	if rindex < lindex:
		return None

	mid  = (lindex+rindex)/2

	if arr[mid] == x:
		return mid

	if arr[lindex] < arr[mid]:#left side is sorted
		if arr[lindex] <= x <=arr[mid]:
			return search(arr, x, lindex, mid-1)
		else:
			return search(arr,x,mid+1, rindex)

	elif arr[lindex] > arr[mid]:#right side is sorted
		if arr[mid] <= x <= arr[rindex]:
			return	search(arr, x, mid+1, rindex)
		else:
			return search(arr,x,lindex, mid-1)
	else:
		res = search(arr,x,lindex,mid-1)
		if res is None:
			return search(arr,x,mid+1,rindex)
		else:
			return res

def main():
	arr = [10,15,20,0,5]
	arr1= [50,5,20,30,40]
	arr2=[2,2,2,3,4,2]
	print
	print search(arr, 5, 0, len(arr)-1)
	print 
	print search(arr1, 5, 0, len(arr1)-1)
	print 
	print search(arr2,4,0, len(arr2)-1)
	print


if __name__=="__main__":
	main()