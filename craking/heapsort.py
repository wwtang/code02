"""
heap sort in python


algorithm: utilizing a heap to index the largest or smallest element, archive the smallest element, 

then re-heapfy the rest elements, and archive the second smallest element. Until no element left.


Given an unordered list, 
1. create a heap of the list, max heap or min heap.
2. remove the smallest one.
3. re-heapfy  the rest elements.


"""

def heap_sort(arr):
	if len(arr) <=1:
		return arr

	first = 0
	last = len(arr)-1

	create_heap(arr,first,last)
	#since it is the max heap, the smallest element is the last one 
	for i in range(last, first, -1):
		arr[i], arr[first] = arr[first], arr[i]
		max_heapfy(arr,first,last-1)
	return arr

def create_heap(arr, first, last):
	"""
	create a heap by heaping from the mid to the start 
	"""
	

	start = (first+last)/2

	while start >= 0:

		max_heapfy(arr, start, last)

		start -=1

def max_heapfy(arr, hp, last):
	"""
	arr is the array
	hp is the heapfy point
	last is the last index of array
	"""

	# 2*i + 1 is the left child
	while 2*hp + 1 <=last:
		k  = 2*hp+1
		#update the largest child of hp
		if k+1 <=last and arr[k] < arr[k+1]:
			k += 1

		#no exchange, hp is the largest data in the triangle 
		if arr[hp] > arr[k]:
			break

		# exchange hp with k(larger child )
		arr[k], arr[hp] = arr[hp], arr[k]
		# move forward and heapfy the point start at k 
		hp = k


def heapsort(a):

    def swap(a,i,j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp  
        
    def siftdown(a, i, size):
        l = 2*i+1
        r = 2*i+2
        largest = i
        if l <= size-1 and a[l] > a[i]:
            largest = l
        if r <= size-1 and a[r] > a[largest]:
            largest = r
        if largest != i:
            swap(a, i, largest)
            siftdown(a, largest, size)
            
    def heapify(a, size):
        p = (size/2)-1
        while p>=0:
            siftdown(a, p, size)
            p -= 1
            
    size = len(a)        
    heapify(a, size)
    end = size-1
    while(end > 0):
        swap(a, 0, end)
        siftdown(a, 0, end)
        end -= 1

    return a 
def main():
	arr = [1,11,4,3,5,66,9]
	print heap_sort(arr)
	print heapsort(arr)

if __name__=="__main__":
	main()

