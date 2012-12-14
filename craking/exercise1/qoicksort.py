"""
"""

def qsort(arr):
	if arr == []:
		return arr

	
	pivot = arr[0]

	lesser =  qsort([i for i in arr[1:] if i < pivot])
	#print lesser
	greater = qsort([i for i in arr[1:] if i >= pivot])
	#print greater

	return lesser+ [pivot]+ greater

def qsort1(arr, first, last):
	if len(arr) == 0 or len(arr) == 1:
		return arr

	if first < last:

		pivot = partition(arr, first,last)
		print "pivot here", pivot

		qsort1(arr, first, pivot-1)

		qsort1(arr, pivot+1, last)

def quick_sort(array):
    
    if len(array) < 2:
        return array
    
    # mid = len(array)/2
    # pivot = array[mid]
    pivot = array[0]
    lesser = [x for x in array if x <pivot]
    greater = [x for x in array if x > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

def partition(arr,first, last):
	i = first -1
	q = last 
	for j in range(first, last):

		if arr[j] <= arr[last]:
			i +=1
			arr[i], arr[j] = arr[j], arr[i]


	arr[i+1], arr[last] = arr[last], arr[i+1]
	print "pivot is ", i+1
	return i+1

def main():
	arr = [16,4,10,14,7,9,3,2,8,1]

	arr1 = [2,8,7,1,3,5,6,4]
	# print arr1
	# qsort1(arr1, 0, len(arr1)-1)
	# print arr1
	print quick_sort(arr1)

if __name__=="__main__":
	main()