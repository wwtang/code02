"""
compress string as letter with its frequency 

if the result not smaller than string , return original string

"""


def compressStr(s):
	if len(s) <1:
		return s

	helper = [0]*256

	for i in range(len(s)):
		index = ord(s[i])
		helper[index] +=1

	res = []
	for j in range(256):
		if helper[j] >0:
			res.append(chr(j))
			res.append(str(helper[j]))



	return "".join(res)

def main():
	s = "aabcccccaaa"

	print compressStr(s)

if __name__=="__main__":
	main()