"""

Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of 
the given array such that the intgers in the subsequence are sorted in increasing order. For example, if input
 is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10},
  then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10



  http://www.geeksforgeeks.org/archives/19248
"""

def MSIS(arr):
	length = len(arr)

	if length<2:
		return arr

	table = arr[:]

	for i in range(1,length):
		for j in range(i):
			if arr[i] > arr[j] and table[i] < table[j]+arr[i]:
				table[i] = arr[i] + table[j]

	return table

def main():
	arr = [1, 101, 2, 3, 100, 4, 5]
	print MSIS(arr)

if __name__=="__main__":
	main()