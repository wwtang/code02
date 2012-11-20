"""
another bubble sort
"""


def f(arr, n):
	"""
	arr is an array with length n
	"""
	#set a global variable x
	x = 0
	trace = []

	if n == 1:
		x == arr[0]

	#deep to the first element of arr through recursive way 
	else:
		f(arr,n-1)

	#the above code can be read as if current index of array is not the first element, deeper one level, 
	#while current index reaches the bottom, enter the second part, that do some manipulation on the current value 

	#trace back

	# second part

	if x > arr[n-1]:
		trace.append(x)
		#print x
		return x
	else:
		trace.append(arr[n-1])
		#print arr[n-1]
		return arr[n-1]


def main():
	arr = [12,10,40,50,100]
	print f(arr,5)

if __name__=="__main__":
	main()