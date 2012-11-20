def func(x):
	if x > 100:
		return x-10
	else:
		return func(func(x+11))



def main():
	print func(99)
	print func(98)
	print func(97)
	print func(91)
	print func(80)
	print func(10)

	print 
	print func(102)
	print func(104)
	print func(108)
	print func(200)
	print func(200000)
if __name__=="__main__":
	main()