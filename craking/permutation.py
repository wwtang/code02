"""

print all the permutation of a string

recursive problem

"a"  ---> a
"a","b" ---> "ab","ba"
"a","b",'c' ---> "abc","acb","bac","bca","cab","cba"

"""


def newPer(singleStr, char):
	"""
	insert char to every slot in the str and append to new string to helper and return it
	"""
	helper = []
	for i in range(len(singleStr)+1):

		newEgg = singleStr[:i] + char + singleStr[i:]
		#print "singleStr slice type", type(singleStr[:i])
		#print "newEgg type", type(newEgg)

		helper.append(newEgg)
	#print "helper type", type(helper)
	return helper

def findPer(str,n):
	"""
	str in the string
	n is the length of the string 
	"""
	if n == 0:
		return None
	if n == 1:
		return [str[n-1]]

	result = []

	for pers in findPer(str,n-1):

		newPers = newPer(pers, str[n-1])

		for p in newPers:

			result.append(p)

	return result

# def generatePer(pers,char):
# 	"""
# 	generate new permutation sets for the pers, which is a permutation sets 
# 	"""
# 	helper = []
# 	for per in pers:
# 		helper.append(newPer(per,char))

# 	return helper






def main():
	str = "ab"
	char = "c"
	#print newPer(str,char)
	print sorted(findPer("abcd",4))

if __name__=="__main__":
	main()