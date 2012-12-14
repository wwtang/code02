"""

Given an array of integers, list out all elements that add up to a given sum X with time complexity O(nlgn)

A = {6,4,5,7,9,1,2}
Sum = 10 Then the pairs are - {6,4} , {9,1}

Two methods:
1, sort the array, two pointer begin from the start and the end
	sorting takes O(nlgn), iteration takes o(n) Overall Nlg(n)

2. dumps the array into dict, compute the difference of givenSum with current value, look up the difference in the dict 
	time complexity O(n)
	space complexity O(n)
"""

def checkSum(arr, gsum):
	if len(arr) ==0:
		return None
	i = 0
	j = len(arr)-1

	#sort the array
	arr.sort()
	res =[]#record the pairs
	while i < j:

		if arr[i]+arr[j] >gsum:
			j -=1
		elif arr[i]+arr[j]<gsum:
			i +=1
		else:
			res.append((arr[i],arr[j]))
			i +=1
			j -=1

	return res


def checkSum2(arr, gsum):
	"""
	use a dict to look
	"""
	if len(arr) ==0:
		return None

	d = dict()

	for v in arr:
		if v not in d:
			d[v] = 1
		else:
			d[v] +=1

	res = []
	for value in arr:
		diff = gsum - value
		if diff in d:
			res.append((value, diff))


	return res

def checkSum3(arr, gsum):
	"""
	use binary search
	"""
	if len(arr) ==0:
		return None

	arr.sort()
	res = []
	for value in arr:
		diff = gsum - value
		other = binarySearch(arr,diff)
		if other:
			res.append((value,other))

	return res

def binarySearch(arr, target):
	if len(arr) == 0:
		return None

	i = 0
	j = len(arr)

	

	while i<=j:
		mid = (i+j)/2

		if arr[mid] > target:
			j = mid-1
		elif arr[mid] < target:
			i = mid+1
		else:

			return arr[mid]


def main():
	arr = [6,4,5,7,9,1,2]
	gsum = 10
	print checkSum(arr, gsum)
	print checkSum2(arr, gsum)
	print checkSum3(arr,gsum)

if __name__=="__main__":
	main()