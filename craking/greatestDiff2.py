"""

Find the greatest diff between a number with the number on its right side. Converting this problem into finding the 
greatest sum of an array.

"""

def greatestDiff(arr, length):

	if arr == None or length < 2:
		return None

	diff = [0]*(length-1)

	for i in range(1,length):

		diff[i-1] = arr[i-1] - arr[i]

	#print diff

	curSum = 0
	greSum = 0

	curSumHelper = []

	greSumHelper = []

	for i in range(len(diff)):

		curSum += diff[i]

		if curSum < 0:
			curSum = 0
			curSumHelper.append(i)

		if curSum > greSum:
			greSum = curSum
			greSumHelper.append(i)

	startIndex = curSumHelper[-1]+1
	endIndex = greSumHelper[-1]

	startIndexOfArr  = startIndex
	endIndexOfArr = endIndex + 1

	print "The greatest sum of arr is %s , which is the difference of %s and %s"%(greSum, arr[startIndexOfArr], arr[endIndexOfArr])

	return greSum

def main():
	arr = [2,4,1,16,7,5,11,9]
	print greatestDiff(arr, len(arr))


if __name__=="__main__":
	main()