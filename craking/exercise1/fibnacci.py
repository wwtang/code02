"""
fibnacci number 

"""

def fib(n):
	"""
	recursive method
	"""
	if n<=0:
		return 0

	if n == 1:
		return 1

	return fib(n-1)+fib(n-2)


def fib1(n):
	"""
	DP
	"""
	table = [0]*(n+1)
	table[1] = 1

	for i in range(2, n+1):
		table[i] = table[i-1] + table[i-2]

	print table 
	return table[n]


def fib2(n):
	"""
	we don't need table here, just need three variables to hold the current values
	"""
	a = 0
	b = 1
	if n<=0:
		return a
	if n == 1:
		return b

	for i in range(2, n+1):
		c = a+b
		a = b
		b = c

	return b

def main():
	print "fibnacci number"
	print fib(5)
	print
	print fib1(5)
	print
	print fib2(5)

if __name__=="__main__":
	main()