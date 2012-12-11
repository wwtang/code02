"""
maximum sum increasing subsequence, similar to longest increasing subsequence 
"""


def msis(d):
	"""
	(list) -->int

	return the maximum sum, just the sum
	"""

	length = len(d)
	if length <2:
		return d

	s = [0]*length	

	for i in range(length):
		MAX = 0
		for j in range(i):

			if d[i] > d[j] and s[j] >MAX :
				MAX = s[j]

		s[i] = d[i]+MAX
			


	SUM = max(s)
	index =  s.index(SUM)

	trace = [index]

	while SUM:
		
		SUM = SUM - d[index]
		if SUM == 0:
			break
		index = s.index(SUM)


		trace.append(index)

	res = []
	for i in trace:
		res.append(d[i])
	res.reverse()

	return res, max(s) 


def main():
	d = [1,101,2,3,100,4,5]
	d1 = [10,5,4,3]
	d2 = [3,4,5,10]

	print msis(d)
	print
	print msis(d1)
	print 
	print msis(d2)

if __name__=="__main__":
	main()










