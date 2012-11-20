

"""
find all the 1 in a number range

find the number of 1 in 1~1000

"""


# def oneCheck(n):
# 	oneCounter = 0
# 	q, r = divmod(n,1)
# 	if q == 1:
# 		oneCounter +=1

# 	return oneCounter


# def tenCheck(n):
# 	tenCounter = 0
# 	tenOneCounter = 0
# 	q,r = divmod(n,10)

# 	if q == 1:
# 		tenCounter +=1

# 	if r == 1:
# 		tenOneCounter +=1

# 	totalCounter =  tenCounter + tenOneCounter

# 	return totalCounter

def onesCounter(a,b):
	"""
	a is the first start number 
	b is the last number 

	"""
	result = 0
	for number in range(a, b+1):
		result += oneOfSingleNum(number)

	return result


def oneOfSingleNum(n):
	length = len(str(n))

	counter = 0
	#append the remainder to the helper
	for i in range(length-1,-1,-1):		
		q , r = divmod(n,pow(10,i))
		n = r
		if q == 1:
			counter +=1


	return counter

def main():
	print oneOfSingleNum(1234212)
	print onesCounter(1,13)
	print onesCounter(0,5)
	print onesCounter(31, 99)


if __name__=="__main__":
	main()
