"""

Given a number determine whether it is a integer

"""
from pprint import pprint

def reverserInt(n):
	rev = 0
	while n > 0:
		rev = rev*10 + n%10
		n /= 10

	return rev



def isParlindrom(n):
	if n < 0:
		return False

	if n < 10:
		return True

	rev = reverserInt(n)

	if rev == n:
		return True
	return False

#more general method

def isParlindrom2(n):
	if n < 0:
		return False

	if n < 10:
		return True
		
	div = 1
	# find the highest digit 
	while n/div > 10:
		div *= 10
		
	#compare the highest and lowest digits 
	while n != 0:

		l = n/div
		r = n%10

		if l!=r:
			return False
		#shrink n and div, remove the highest and lowest digits 
		 	
		n = (n%div)/10
		div /=100

	return True

def stringIsParlindrom(str):
	l = len(str)
	if l == 1:
		return True

	left = 0
	right = l-1
	while left<= right:
		if str[left] !=str[right]:
			return False
		left +=1
		right -=1
	return True


def longestParlindrom(str):
	"""
	find the longest palindromic string of the given string

	if use brute force method, there are total 2(n) substrings, so the runtime at lease o(2(n))

	Apply Dynamic programming. create table[i][j], i is the start index, j is the end index
	fill the table by diagonal, begin from the main diagonal, which means the substring with length 1
	then length 2, 3 ... to the end 
	"""
	length = len(str)
	table = [0]*length
	row = [0]*length

	for i in range(length):
		table[i] = row[:]

	#fill the main diagonal with 1. All substring with length 1 is palindrome
	maxLength = 1
	start = 0

	for i in range(length):
		table[i][i] = 1

	#fill the second diagonal, all subString with length 2

	for i in range(length-1):
		if str[i] == str[i+1]:
			table[i][i+1] =1
			maxLength = 2
			start = i

	# define the length first, k is the length of substring
	for k in range(3,length):
		for i in range(length-k):
			# j is the end of each substring
			j = i+k-1
			if str[i] == str[j] and table[i+1][j-1] == 1:
				table[i][j] = 1

				if k > maxLength:
					start = i
					maxLength = k

	res = str[start:start+maxLength]
	# pprint(table)
	return res
	


def main():
	n = 123
	n1 = 12121
	print isParlindrom(n)
	print isParlindrom(n1)
	print isParlindrom2(n)
	print isParlindrom2(n1)
	str = "caooac"
	s1 = "gunniinnug"

	print stringIsParlindrom(str)
	print stringIsParlindrom(s1)
	str2 = "forgeeksskeegfor"

	print longestParlindrom(str2)
	str3 = "abbefg"
	print longestParlindrom(str3)
if __name__=="__main__":
	main()