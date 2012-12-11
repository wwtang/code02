"""
LIS longest increasing subsequence 
"""


def findLIS(lst):
	length = len(lst)
	LIS = [1]*length
	track = []


	for i in range(length):

		for j in range(i):
			if lst[i] > lst[j]:

				LIS[i] = max(LIS[:i]) + 1 
				track.append(lst[i])
				#print "we are here", LIS[i]
			else:
				LIS[i] = 1
	print track
	return LIS 


def main():
	lst = [10, 22, 9, 33, 21, 50, 41, 60, 80]

	lst1 = [2,1,5,3,6,4,8,9,7]
	#lst  = [10 ,22]
	print findLIS(lst)
	#print findLIS(lst1)

if __name__=="__main__":
	main()