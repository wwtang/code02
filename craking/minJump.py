"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.



"""

def minJump(arr, low, high):
	"""
	arr is the input array
	low is the begin index
	high is the last index
	(list, int, int) -->int

	>>> arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	>>> low = 0
	>>> high = len(arr)-1
	>>> high = 10
	>>> minJump(arr, low, high)
	3
	"""
	inf = float('inf')

	if arr[low] == 0:
		return inf

	if low == high:
		return 0

	Min = inf

	i = low +1

	while i <= high and i<= low + arr[low]:
		jumps = minJump(arr, i, high)

		if jumps != inf and jumps +1 < Min:
			Min = jumps +1

		i +=1
	return Min
def main():
	arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	low = 0
	high = len(arr)-1
	print minJump(arr, low, high)

if __name__ == "__main__":
	main()
   	import doctest
   	doctest.testmod()

