"""
longest increasing subsequence

use max to get the max element 

"""

def LIS(arr):

	length = len(arr)

	if length < 2:
		return length

	table = [0]*length

	table[0] =1

	for i in range(length):
		for j in range(i):

			if arr[i] >arr[j]:

				table[i] = max(table[:i]) +1

			else:
				table[i] =1


	return table, max(table)

def main():
	arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
	arr1 = [1,2,5,3,4]
	print LIS(arr1)

if __name__=="__main__":
	main()
