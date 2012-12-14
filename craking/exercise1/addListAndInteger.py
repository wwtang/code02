"""
Given a list of integer ex:[1,2,3] and an integer ex:45
write a function of add([1,2,3], 45), and return [1,6,8]

Analysis:

1. Analysis all the basic cases....
2. write a helper function to convert the second argument, the integer, into list representation.
	ex: toDigits(45) --> [4,5]

3. all the tow lists and be careful with the carry.	

"""

def toDigits(num):
	"""
	int --> list
	>>>toDigits(45)
	[4,5]
	>>>toDigits(536)
	[5,3,6]
	"""
	
	return [int(i) for i in list(str(num))]

def add(arr, num):

	#extreme cases

	arr2 = toDigits(num)

	carry = 0
	res = []
	while arr and arr2:
		tmp = arr.pop()+ arr2.pop()+carry
		if tmp >10:
			carry = 1
			tmp %= 10
		else:
			carry =0 
		res.append(tmp)

	return res






def main():
	# print toDigits(45)
	# print toDigits(-234)
	print toDigits(100)
	print add([5,8],44)
	

if __name__=="__main__":
	main()