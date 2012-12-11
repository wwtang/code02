"""
find all the substring of a string, exclude empty one

"""

def substr(s):
	length = len(s)

	if length <=1:
		return s

	res = []

	for i in range(length):
		tmp = s[i]
		res.append(tmp)
		for j in range(i+1, length):
			tmp = tmp + s[j]
			res.append(tmp)

	return res

def main():
	s = "abcd"
	print substr(s)

if __name__=="__main__":
	main()