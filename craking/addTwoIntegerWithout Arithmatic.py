"""
implement the add method of two integers without arithmetic 
bit operation 

"""

import time

def printTime(func):

	def newfunct(*args):
		startTime = time.clock()
		func(*args)
		endTime = time.clock()

		print "run time of function %s is %s"%(func.__name__, (endTime-startTime)*1000.0)
		return func(*args)


	return newfunct



@printTime
def addWithoutArithemeticWrapper(a,b):
	return addWithoutArithmetic(a,b)


def addWithoutArithmetic(a, b):
	if b == 0:
		return a

	sumWithoutCarry = a^b

	carry = a & b 

	return addWithoutArithmetic(sumWithoutCarry,carry<<1)


@printTime
def addfunc(a,b):
	return a+b

def main():
	print addWithoutArithemeticWrapper(3,5)
	print addfunc(3,5)

if __name__=="__main__":
	main()