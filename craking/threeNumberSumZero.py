"""
For an array that contains positive and negative integers, find a tuple of three number that their sum is Zero

"""


def sumZero(arr):
	if len(arr) <3:
		return None

	arr.sort()

	length = len(arr)

	for i in range(length-2):

		j = i+1
		k = length-1
		while j<k:
			tup = [arr[i],arr[j],arr[k]]
			if sum(tup) == 0:
				return(arr[i],arr[j],arr[k])

			else:
				if sum(tup)>0:
					k -=1
				else:
					j+=1
	print "no such tuple in the arrar"
	return None 


def main():
	arr = [-8,7,-3,10,4,5,-1,-2,6]
	print sumZero(arr)

if __name__=="__main__":
	main()

