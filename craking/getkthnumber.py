"""
get Kth number that only primes are 3 ,5  7
"""
import time 

def printTime(func):
	def wrapper(args):
		startTime = time.clock()
		res = func(args)
		endTime = time.clock()
		print "The run time of %s is %s"%(func.__name__, (endTime-startTime)*1000)
		return res
	return wrapper


def removeMin(lst):
	"""
	return and remove the smallest number of the list
	"""
	minNum = min(lst)

	while minNum in lst:
		lst.remove(minNum)

	return minNum


def addNewNumber(lst, v):
	"""
	v is the smallest number is lst, add v*3, v*5 and v*7 into lst
	"""

	lst.append(v*3)
	lst.append(v*5)
	lst.append(v*7)

@printTime
def getKthNum(k):
	"""
	k is the index of kth ugly number
	"""
	helper = [1] # 1 is the first number fit requirement 

	if k < 0:
		return None
	val = helper[0]
	for i in range(1,k+1):
		val = removeMin(helper)
		addNewNumber(helper, val)

	return val 


@printTime
def getKthNumber2(k):
	"""
	optimized solution, 1 is the actual first ugly number, so Kth here is actually k+1 th number  
	"""
	if k <0:
		return None

	#initialize three lists
	Q3 = [3]
	Q5 = [5]
	Q7 = [7]
	for i in range(1,k+1):
		minNumber = min(Q3[0],Q5[0],Q7[0])

		if minNumber == Q3[0]:
			Q3.append(3*minNumber)
			Q5.append(5*minNumber)
			Q7.append(7*minNumber)
			Q3.pop(0)

		elif minNumber == Q5[0]:
			Q5.append(5*minNumber)
			Q7.append(7*minNumber)
			Q5.pop(0)
		else:
			Q7.append(7*minNumber)
			Q7.pop(0)

	return minNumber


def main():
	k = 100

	kth = getKthNum(k)
	
	print kth
	print 
	kth2 = getKthNumber2(k-1)
	print kth2

if __name__=="__main__":
	main()