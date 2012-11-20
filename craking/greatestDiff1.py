"""

The greatest difference of an arr

divide and conquer 
"""

def MaxDiff(arr, length):
	if arr is None or length < 2:
		return None
	Max = 0
	Min = 0
	return MaxDIffMethod(arr, arr+length-1, Max, Min)


def MaxDIffMethod(start, end, Max, Min):

	if start == end:
		