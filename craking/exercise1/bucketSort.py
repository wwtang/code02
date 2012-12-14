"""
bucket sort

"""

def bucketSort(arr, m):
	"""
	arr is the array need to be sorted.
	m is the number of bucket.
	"""
	if len(arr)<2:
		return arr
	
	buckets = [[] for i in range(m)]

	#allocate the data into different buckets according to their value
	for v in arr:
		buckets[v/m].append(v)

	#sort each bucket and then merge them together 
	res = []
	for bucket in buckets:
		bucket.sort()
		res.extend(bucket)

	return res


def main():
	from random import randint
	arr = [randint(0,99) for i in range(30)]
	m = 10
	print "before sorting,", arr
	print "after sorting"
	print bucketSort(arr, m)

if __name__=="__main__":
	main()

