def func(x):
	if x > 0:
		func(x -=1)
		print x 
		func(x -=1)


def main():
	func(4)

if __name__=="__main__":
	main()