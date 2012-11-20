"""
quick sort ex
run time nlg(n)
"""

def quicksort(arr):
	length = len(arr)
	return qsort(arr, 0, length-1)

def qsort(arr, lindex, rindex):
	if len(arr) == 1 or len(arr) == 0:
		return arr
	
	if lindex <= rindex:
		pivot = partition(arr, lindex, rindex)
		qsort(arr, lindex, pivot-1)
		qsort(arr, pivot+1, rindex)
	return arr


def partition(arr, q, r):
	i = q-1
	p = arr[r]
	# j to the second last one 
	for j in range(q,r):
		if arr[j] <= p:
			i +=1			
			arr[i], arr[j] = arr[j], arr[i]
	# list is mutable, use arr[r] instead of p 					
	arr[i+1], arr[r] = arr[r], arr[i+1]
	return i+1

	


def main():
	arr = [2,8,7,1,3,5,6,4]
	res = quicksort(arr)
	print res

if __name__=="__main__":
	main()