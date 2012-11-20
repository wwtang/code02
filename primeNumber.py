"""
1.Determine if a number is a prime number 

	let the target number n  mods every number from 2 to n's sqrt root, if mod == 0, not prime, else is prime number 
2. Find all the prime number that less than the given number


"""
import math

def isPrime(num):
	if num <2:
		return False

	#get the sqrt root
	sqrtRoot = int(math.sqrt(num)+1)
	for i in range(2, sqrtRoot):
		if num % i==0:
			return False
	return True

def findAllPrimeNumber(tnum):
	"""
	find and print all the prime number less than tnum(target number)
	"""
	#set flags 
	flags = [True]*tnum
	flags[:2] = False, False
	#first prime 

	primeNum =  2

	while primeNum<tnum:
		# corssoff the remain numbers
		crossOff(flags, primeNum)

		#update prime
		primeNum = getNextPrime(flags, primeNum)


		if primeNum > len(flags):
			break

	return flags



# cross off 
def crossOff(flags, primenum):
	""" begin startNum, find all the multiplies of the prime number by  "prime*prime + prime """

	startNum = primenum*primenum
	length = len(flags)
	gap = primenum

	for nextNum in range(startNum, length, gap):
		flags[nextNum] = False

#get the next prime number 
def getNextPrime(flags, primeNum):
	next = primeNum +1
	while next < len(flags) and not flags[next]:
		next +=1
	return next 

def printOutPrime(flags):
	result = []
 	for i in range(len(flags)):
 		if flags[i] == True:
 			result.append(i)
 	return result


def test(got, expect):
	if got == expect:
		print "OK"
	else:
		print "Expect %s, but got %s" %(expect, got)


def main():
	# arr = [4,5,6,7,8,9,11,13,42,100,101,False]
	# expect =[False, True, False, True,False,False,True,True,False,False,True,False]

	# result = []
	# for num in arr:
	# 	result.append(isPrime(num))

	# #test
	# for i in range(len(arr)):
	# 	test(expect[i],result[i])
	# print result
	

	result1 = findAllPrimeNumber(100)

	primeNumbers = printOutPrime(result1)

	for num in primeNumbers :
		print isPrime(num)
	


if __name__=="__main__":
	main()



