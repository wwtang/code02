"""

1. brute-force   O(m*n)
2. apply binary search for each element of array1 into array2 m*log(N)
3. load arr1 to hash table, and then check the element in array2 with the hash table O(m+n) 
4. Due to both the array are sorted, we can check them one by one with index i and j

	if arr1[i] > arr2[j]:
		j +=1
	elif arr1[i] < arr2[j]:
		i +=1
	else:
		i +=1
		j+=1
		res. append(arr1[i])
"""

def intersectionOfTwoArrays(arr1, arr2):
	length1 = len(arr1)
	length2 = len(arr2)

	if length1 ==0 or length2 == 0 or arr1[-1] < arr2[0] or arr1[0] > arr2[-1]:
		return []

	i = 0
	j = 0
	res = []
	while i < length1 and j < length2:

		if arr1[i] < arr2[j]:
			i +=1
		elif arr1[i] > arr2[j]:
			j +=1
		else:
			res.append(arr1[i])
			i +=1
			j +=1
	return res

def main():
	arr1 = [1,2,3,4,5,6]
	arr2 = [3,4,6,7,8,9]
	arr3 =[]
	arr4 = [7,8,9]

	print intersectionOfTwoArrays(arr1,arr2)
	print intersectionOfTwoArrays(arr3,arr4)
	print intersectionOfTwoArrays(arr1,arr3)
	print intersectionOfTwoArrays(arr2, arr4)
if __name__=="__main__":
	main()
