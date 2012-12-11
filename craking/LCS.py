"""

Longest common subsequence 
There are two helper arrays in this algorithm, c[i][j] and d[i][j].
c[i][j] represent the length longest common subsequence of string x at index i and string y at index j, which is 

c[i][j] = {
		0						if i =0 or j = 0
		c[i-1][j-1] + 1 		if x[i] = y[j]
		max{c[i-1][j],			if x[i] != y[j]
		 c[[i][j-1]]}
		}

d[i][j] records the location that found a new match of characters for x and y, and  can be represented as:

d[i][j] = {
	
	2 			if c[i][j] = c[i-1][j-1] +1
	1 			else
}


print out one of the longest common subsequence according to the array d 

"""
from pprint import pprint 

def lcs(x, y):
	"""
	(str, str) --> list
	"""
	m = len(x)
	n = len(y)
	

	if m < 1 or n < 1:
		return None

	row = [(0,'-')]*(n+1)
	c = [0] * (m+1)

	for i in range(m+1):
		c[i] = row[:]

	

	for j in range(n+1):
		for i in range(m+1):
			if i == 0 or j == 0:
				c[i][j] = (0,"*")
			elif x[i-1] == y[j-1]:
				c[i][j] = ((c[i-1][j-1][0] +1), "\\")
			else:
				
				Max = c[i-1][j][0]

				if c[i][j-1][0] > Max:
					c[i][j] = (c[i][j-1][0], '-')
				else:
					c[i][j] = (c[i-1][j][0], '|')


		

	pprint(c)
	print
	print x 
	print y

	i = m
	j = n
	res = []
	length = c[m][n][0]

	while j >=0:
		if c[i][j][1] == "\\" and c[i][j][0] == length:
			res.append(y[j-1])
			j -=1
			k = i -1
			length -=1

		i -=1

		if i == 1:
			i = k
			j -=1
	res.reverse()
	return res


def main():
	x = "ABCBDAB"
	y = "BDCABA"

	print lcs(x,y)

if __name__=="__main__":
	main()



