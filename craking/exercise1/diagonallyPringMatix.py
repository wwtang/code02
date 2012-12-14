"""
diagonally print the matrix 
similar to longest palindrome 

"""

def printMatrix(mtr):

	if len(mtr) == 0:
		return None

	length = len(mtr)
	res = []
	for k in range(1,length+1):#is the length of 
		for i in range(length-k+1):
			j = i+k-1
			res.append(mtr[i][j])
		print res
		res = []
			#print mtr[i][j]

def main():
	mtr = [[1,2,3,4],[11,22,33,44],[111,222,333,444],[1111,2222,3333,4444]]
	printMatrix(mtr)

if __name__=="__main__":
	main()