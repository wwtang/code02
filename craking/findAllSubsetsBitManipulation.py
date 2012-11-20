"""
find all the subsets use bit manipulation
"""

def getSubsets(s):
	"""
	s is  the string or set
	"""
	res = []
	if len(s) <1 :
		return res 
	
	Max = 1 << len(s)

	for i in range(Max):
		subset = bitToSet(i, s)
		res.append(subset)

	return res


def bitToSet(x, s):
	res = []

	k = x
	bitIndex = 0
	while k >0:
		if k & 1 == 1:
			res.append(s[bitIndex])

		k >>=1
		bitIndex +=1

	return res 

def pprint(s):
	sets = getSubsets(s)
	res = []
	for elem in sets:
		res.append("".join(elem))
	return	res 


def main():
	string = "adf"
	
	print pprint(string)
	



if __name__=="__main__":
	main()