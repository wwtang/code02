def func(x):
	if x > 0:
		# x -=1
		func(x-1)
		print x 
		# x -=1
		func(x-1)

def main():
	func(4)
	# print 
	# func(2)
	# print
	# func(5)

if __name__=="__main__":
	main()


