"""
fib numbers in memorization and tabulation version 
"""


def fib1(n, lookup):
	"""memorization version"""		
	if n <=1:
		lookup[n] = n
	else:
		lookup[n] = fib1(n-1,lookup) + fib1(n-2,lookup)
		#print
		#print lookup
	return lookup[n]


def fib2(n):
	"""tabulation version, no recursive here """
	f = [None]*(n+1)
	i = 0
	f[0] = 0
	f[1] = 1
	for i in range(2,n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

def main():
	n = 10

	lookup = [None]*(n+1)
	print fib1(n, lookup)
	print 
	#print lookup
	print 
	print fib2(n)



if __name__=="__main__":
	main()