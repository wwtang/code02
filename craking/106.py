"""
write a method to find a given number in double sorted matrix

arr = [[15, 20, 40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
find 55

method 1: apply binary search to each row 
"""

def binarySearch(arr, target, first ,last):
	if last < first or len(arr) <0 or target == None:
		return None

	mid = (first + last)/2

	if arr[mid] == target:
		return mid
	elif target < arr[mid]:
		return binarySearch(arr, target, first, mid-1)
	else:
		return binarySearch(arr, target, mid+1, last)

def findElem(arr, target, height, length):
	""" height is the number of list in arr, and the length is the length of list"""
	if arr == None or len(arr) <1 or target == None:
		return None

	for i in range(height+1):# height = len(arr) -1, and range(height) = len(arr)-1-1
		j = binarySearch(arr[i], target, 0, length)
		if j:
			return (i,j)

	return none

def findElem2(arr, target, row, col):
	"""
	row = len(arr) -1 
	col = len(arr[0]) -1 
	"""
	if arr == None or len(arr) < 1 or target == None:
		return None

	i= 0 
	j = col
	while i <=row and j >=0:
		if arr[i][j] == target:
			return (i,j)
		elif target > arr[i][j]:
			i +=1
		else:
			j -=1

	return None 


def main():
	arr = [[15, 20, 40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
	height = len(arr)-1
	length = len(arr[0]) -1
	print findElem(arr, 55, height, length)
	print "The second method:"
	print findElem2(arr, 55, height, length)
	# arr1 = [15, 20, 40,85]
	# print binarySearch(arr1, 40, 0, len(arr1)-1)
	# print binarySearch(arr1, 85, 0, len(arr1)-1)


if __name__=="__main__":
	main()