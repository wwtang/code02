"""

given an array find the magic index.
Magic index is defined as: for an index in array A, if A[i] == i, i is the magic index
(value in array is distinct )

follow up:
(value in the array are not distinct)

"""


def findMagic(arr, lindex, rindex):
	#define the bound condition 
	if len(arr) <1 or lindex > rindex:
		print "bound condition"
		return None

	mid = (lindex+rindex)/2


	if arr[mid] == mid:

		return mid
	elif arr[mid] > mid:#search left
		print "search left side "

		return findMagic(arr, lindex, mid-1)
	else: #search right side
		print "search right side"

		return findMagic(arr, mid+1,rindex)

#non-distinct scenario

def findMagicPro(arr,lindex,rindex):
	
	if len(arr) < 1 or rindex < lindex:
		return None

	mid = (lindex+rindex)/2

	if arr[mid] == mid:
		return mid


	leftEnd = min(mid-1, arr[mid])

	left = findMagicPro(arr, lindex,leftEnd)
	if left >= 0:
		return left


	rightStart = max(mid+1, arr[mid])
	print "rightStart", rightStart
	right = findMagicPro(arr,rightStart, rindex)

	return right



def main():
	arr = [-40,-20,-1,1,2,3,5,7,9,12,13]

	#print findMagic(arr, 0, len(arr)-1)

	arr2 = [-10,-5,2,2,2,3,4,7,9,12,13]
	print findMagicPro(arr2, 0, len(arr2)-1)

if __name__=="__main__":
	main()