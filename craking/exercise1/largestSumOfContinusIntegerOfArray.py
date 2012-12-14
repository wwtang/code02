"""
Find the largest sum of consecutive integers in an array?
all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). 
Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far
O(n), dynamic programming
{-2, -3, 4, -1, -2, 1, 5, -3} -->[4,-1,-2,1,5] = 7
>>>arr = [-2, -3, 4, -1, -2, 1, 5, -3]
>>>arr1 = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
>>>largestSum(arr)
7
>>>largestSum(arr1)
17

"""

def largestSum(arr):
	if len(arr) == 0:
		return None

	#tow flags, 
	maxSumEndHere = 0
	#trace the max sum of all the maxSumEndHere
	maxSum  = 0

	for i in range(len(arr)):
		maxSumEndHere = max(0, maxSumEndHere+ arr[i])# maxSumEndHere ==0 means the value before i has no contribution to the largest sum

		if maxSum < maxSumEndHere:
			maxSum = maxSumEndHere


	return maxSum if maxSum >0 else max(arr)


def main():
	arr = [-2, -3, 4, -1, -2, 1, 5, -3]
	arr1 = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
	arr2 = [-1,-2,-3,-4,-10,-2]
	print largestSum(arr)
	print largestSum(arr1)
	print largestSum(arr2)

if __name__=="__main__":
	main()