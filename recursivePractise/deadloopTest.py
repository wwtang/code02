"""
Test for dead loop
"""

def func(n):
	if n%2==0:
		n +=1
		return n
	else:
		print "we are here"
		return func(func(n-1))


def main():
	print func(2)
	#print func(3)

if __name__=="__main__":
	main()