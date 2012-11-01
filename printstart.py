"""
"""


def func(n):

	if n >1:
		func(n-1)

	for i in range(n):
		print i
		print "*"
		print 

def main():
	print func(5)

if __name__=="__main__":
	main()