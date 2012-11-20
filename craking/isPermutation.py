"""
check if a string is permutation of the other
4 mehtods
"""

def isPer(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	if len1 != len2:
		return False

	s1 = list(str1)
	s1.sort()
	s2 = list(str2)
	s2.sort()

	if s1 == s2:
		return True
	else: 
		return False

def histgram(s):
	if len(s)<1:
		return None

	res = {}

	for l in s:
		if l not in res:
			res[l] =1
		else:
			res[l] +=1

	return res

def isPer1(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	if len1 != len2:
		return False

	d1 = histgram(str1)
	d2 = histgram(str2)

	if d1 != d2:
		return False
	else:
		return True


def countLetter(s):
	helper = [0]*26
	for letter in s:
		index = ord(letter)-ord("a")#only lower case
		helper[index] +=1
	return helper

def isPer2(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	if len1 != len2:
		return False

	c = countLetter(str1)
	#c2 = countLetter(str2)
	for i in range(len(str2)):
		index= ord(str2[i])- ord("a")
		c[index] -=1

		if c[index] <0:
			return False
	return True 





def main():
	s1= "caonima"
	s2 = "nimacao"
	s3 = "shabi"
	s4= "shanimei"


	print isPer(s1,s2)
	print isPer1(s1,s2)
	print isPer2(s1,s2)
	print 
	print isPer(s3,s4)
	print isPer1(s3,s4)
	print isPer2(s3,s4)
	
if __name__=="__main__":
	main()
