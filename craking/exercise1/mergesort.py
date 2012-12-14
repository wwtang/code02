"""
"""

def mergeSort(arr, first, last):

	if len(arr)<2:
		return arr

	mid = (first+last)/2

	if first <last:

		left = mergeSort(arr, first, mid-1)
		right = mergeSort(arr, mid+1, last)

		merge(left, right)


def merge(arr1, arr2):
	"""

	arr1 and arr2 are well sorted array,
	"""
	res = []

	i = j = 0

	while i< len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			res.append(arr1[i])
			i+=1
		else:
			res.append(arr2[j])
			j+=1

	while i < len(arr1):
		res.append(arr1[i])
		i +=1

	while j < len(arr2):
		j +=1
		res.append(arr2[j])

	return res


def main():
	arr = [2,8,7,1,3,5,6,4]
	print mergeSort(arr, 0, len(arr)-1)

if __name__=="__main__":
	main()



