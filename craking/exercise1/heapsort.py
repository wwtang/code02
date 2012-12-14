"""
heapsort 

first, write the max heapify function, which takes O(lg(n))
second, build a max heap, which costs O(n)
And then, retrieve the max value, and re-heapify the rest heap, overall runtime is O(nlgn)

"""

def maxHeapify(arr,i,last):
	"""
	arr is the input arr,
	i is the index from which start to heapify
	heapify will not return any object, but modify the order of element in the array 

	"""
	l = 2*i
	r = 2*i +1
	if l <= last and arr[l] > arr[i]:
		largest = l
	else:
		largest	= i

	if r <= last and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[largest], arr[i] = arr[i], arr[largest]

		maxHeapify(arr, largest,last)

def buildMaxHeap(arr):
	"""
	apply maxHeapify to each parent node of the array, and build a max heap, which means
	the top element of the heap is the largest element.
	Similar to maxHeapify, build max heap will not return any object, but modify the order
	of the elements.
	"""
	last = len(arr)-1
	sizeArr = len(arr)-1
	# arr[sizeArr/2] is the last parent node 
	for i in range(sizeArr/2, -1, -1):
		maxHeapify(arr, i, last)


def heapSort(arr):
	sizeArr = len(arr)
	if sizeArr < 2:
		return arr 

	last = sizeArr-1
	buildMaxHeap(arr)
	# for i = arr.length downto 2
	while last>0:
		
		
		arr[0], arr[last] = arr[last], arr[0]
		last -=1
		maxHeapify(arr, 0,last)

	# for i in range(last,0,-1):
	# 	arr[0],arr[i] = arr[i],arr[0]
	# 	maxHeapify(arr,0,i-1)

def main():
	arr = [4,1,3,2,16,9,10,14,8,7]
	print arr
	buildMaxHeap(arr)
	print 
	print 
	print arr
	
	heapSort(arr)
	print arr

	# arr1 = [7, 14, 9, 10, 8, 1, 4, 2, 3]
	# print arr1
	# print
	# maxHeapify(arr1,0)
	# print arr1

if __name__=="__main__":
	main()








