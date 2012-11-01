"""

Given a sorted array of string which was interspersed with empty string, write a method to find 
the location of given string

input ["at","","","", "ball","","", car","", "", "dad","",""]
find ball return 4

This is a binary search problem, what you need to do is apply binary search in different scenarios


mid = (left+right)/2



"""

def findStr(arr, str, first, last):
	"""find index of str in arr, and return its index. It is a good idea to introduce new index
		for different part.
	"""
	if len(arr) <0 or str == "":
		return None


	mid = (first + last)/2
	# if arr[mid] is empty string, initialize two index left and right 
	left = mid
	right = mid
	if mid == "":
		left = mid -1# index used for left part
		right = mid +1# index for right part

	#find the closest non-empty string of mid and update mid
	while True:
		#print "we entered while loop and the left = %d, right=%d, mid= %d"%(left, right, mid)
		if left < first and right > last:
			return None
		elif left >= first and arr[left] != "":
			mid = left
			break
		elif right <= last and arr[right] != "":
			mid =right
			break
		left -=1
		right +=1

	#print "updated mid: ", mid
	#search the arr in binary search way
	if arr[mid] == str:
		return mid
	elif arr[mid] < str:
		return findStr(arr, str, mid+1, last)
	else:
		return findStr(arr, str, first, mid-1)



def test(got, expect):
	if got == expect:
		print "OK"
	else:
		print "Got %s, but expect %s "%(got, expect)

def main():

	arr = ["at","","","", "ball","","", "car","", "", "dad","","","","fog"]
	#first is 0 and last is len(arr) -1
	test(findStr(arr, "at", 0, len(arr)-1),0)
	test(findStr(arr, "ball", 0, len(arr)-1),4)
	test(findStr(arr, "car", 0, len(arr)-1),7)
	test(findStr(arr, "dad", 0, len(arr)-1),10)
	test(findStr(arr, "fog", 0, len(arr)-1), 14)
	

if __name__=="__main__":
	main()




