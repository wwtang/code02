"""

Find the substring of string with largest sum 

input: an array with positive and negative integer,

output the largest sum of a substring of the array 


algorithm:

two flags : current sum and largest sum

1. Go through the array from the first integer, and add to current sum, if curSum < 0, set curSum to 0, else largestSum = curSum
2. if the result of the first step is negative, then go through the array to find the largest number 
"""


def findLargestSum(arr, length):
	if length < 1:
		return None

	CursubStr = []
	LarsubStr = []

	CurSum = CurLargestSum = 0

	for i in range(length):
		CurSum += arr[i]

		if CurSum < 0:

			CursubStr.append(i)

			CurSum = 0

		if CurSum > CurLargestSum:

			LarsubStr.append(i)
			CurLargestSum =  CurSum 

	if CurLargestSum == 0:
		CurLargestSum = arr[0]
		for i in range(length):
			if arr[i] >=CurLargestSum:
				CurLargestSum = arr[i]

	startIndex = CursubStr[-1] +1
	endIndex  = LarsubStr[-1]



	return CurLargestSum, (startIndex, endIndex)

def main():

	arr = [1,-2,3,10,-4,7,2,-5]
	print findLargestSum(arr, len(arr))



if __name__=="__main__":
	main()