"""
find the longest palindromic substring 

http://www.geeksforgeeks.org/archives/25463

"""
from pprint import pprint 

def LPS(s):
	length = len(s)

	if length <2:
		return s 
	counter = 0
	tab =[0]*length
	row = [0]*length

	for i in range(length):
		tab[i] = row[:]


	#all the single character is palindromic substring
	for i in range(length):
		counter +=1 
		tab[i][i] = 1


	start = 0 
	maxLength = 1
	#check all the substring with length 2 
	for i in range(length-1):
		if s[i] == s[i+1]:
			tab[i][i+1] = 1
			counter +=1
			start = i

			maxLength = 2

	print "start here ",start

	for k in range(3, length):

		for i in range(length-k):
			j = i+k-1
			if s[i] == s[j] and tab[i+1][j-1] == 1:
				tab[i][j] = 1
				counter +=1

				if k > maxLength:
					start = i
					maxLength = k

	print 'start and maxLength %s %s'%(start, maxLength)

	printout(s, start, maxLength + start -1 )
	return tab, counter

def printout(arr, start, end):

	for i in range(start, end+1):
		print arr[i]


def main():
	s = "ababbbabbababa"
	s1 = "forgeeksskeegfor"
	pprint(LPS(s1))

if __name__=="__main__":
	main()



