"""
determine whether a string is palindromic, two methods

"""

def isPalindromic(s):
	length = len(s)

	if length<2:
		return False

	sre = s[::-1]
	if cmp(s,sre) != 0:
		return False
	return True


def isPalindromic2(s):
	length = len(s)

	if length <2:
		return False
	i = 0
	j = length -1
	while i <=j:
		if s[i] != s[j]:
			return False
		i +=1
		j -=1

	return True


def main():
	s = "abc"
	s1 = "aba"
	s2= "a"
	s3 = "geeksskeeg"

	print isPalindromic(s)
	print isPalindromic2(s)
	print 
	print isPalindromic(s1)
	print isPalindromic2(s1)
	print
	print isPalindromic(s2)
	print isPalindromic2(s2)
	print
	print isPalindromic(s3)
	print isPalindromic2(s3)


if __name__=="__main__":
	main()