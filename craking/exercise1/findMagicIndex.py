"""
find magic index

1. distinct 
2. not distinct 

"""


def findMagic(arr, start, last):
	if start > last or start <0 or last > len(arr):
		return None

	mid = (start+last)/2

	if arr[mid] == mid:
		return mid

	elif arr[mid] > mid:
		return findMagic(arr, start, mid-1)
	else:
		return findMagic(arr, mid+1, last)


def findMagic1(arr):

	if len(arr)<0:
		return None
	first =0
	last = len(arr)-1

	
	while first <= last:

		mid =(first+last)/2
		if arr[mid] == mid:
			return mid
		elif arr[mid]>mid:
			last = mid-1
		else:
			first = mid+1

	return None

def findMagicNotDistinct(arr, first,last):
	if first > last or first <0 or last>len(arr)-1:
		return None

	midIndex = (first+last)/2
	midValue  = arr[midIndex]

	if midIndex == midValue:
		return midIndex

	left = findMagicNotDistinct(arr, first, min(midValue, midIndex-1))
	if left>=0:
		return left

	right = findMagicNotDistinct(arr, max(midValue, midIndex+1), last)
	return right
def main():
	arr = [-40, -20,-1,1,2,3,5,7,9,12,13]
	print findMagic(arr, 0, len(arr)-1)
	print findMagic1(arr)
	arrnot = [-10,-5,2,2,2,3,4,7,9,12, 13]
	print findMagicNotDistinct(arrnot, 0, len(arrnot)-1)

if __name__=="__main__":
	main()