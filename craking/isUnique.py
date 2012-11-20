"""
isUnique,
use boolean flags

"""

def isUnique(s):
	if len(s) > 256:
		return False

	flags = [False]*256

	for i in range(len(s)):
		index = ord(s[i])

		if flags[index]:
			return False

		flags[index] = True

	return True



def main():
	s = "abcdgef"
	s1 = "aaabbcd"
	s2 = "abcdesa"

	print isUnique(s)
	print isUnique(s1)
	print isUnique(s2)

if __name__=="__main__":
	main()