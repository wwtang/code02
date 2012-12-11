"""
LIS in nlog(n) method

Utilize a helper list B, B[L] represents the longest increasing substring with length L at current index 

you can visit http://www.felix021.com/blog/read.php?1587 for detail


"""

def LIS(d):
	"""
	(list) --> int
	d is the input array 
	return the length of the LIS
	"""

	if len(d) <2:
		return d
	length = len(d)
	B = [0]*length

	B[1] = d[0]# d[0] can build a LIS with length 1
	L = 1
	for i in range(1, length):
		if B[L] > d[i]:
			B[L] = d[i]
		else:
			L +=1
			B[L] = d[i]
	return L


def LIS2(arr):
	"""
	Utilize binary search to find the position of arr in helper list B which runtime is log(n)
	total runtime is nlog(n)

	"""
	length = len(arr)
	if length < 2:
		return length 
	B = [0]*length 

	L = 1 
	B[0] = arr[0]

	for i in range(1, length):
		left = 0
		right = L

		while left <= right:
			mid = (left+right)/2
			if B[mid] < arr[i]:
				left = mid +1
			else:
				right = mid-1
		print "left", left
		B[left] = arr[i]
		if left > L:
			L +=1
	return L



def main():
	d = [2,1,5,3,6,4,8,9,7]

	print LIS(d)
	print
	print LIS2(d)

if __name__=="__main__":
	main()