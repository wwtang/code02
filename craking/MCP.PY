"""
matrix chain product problem.
Calculate the product of matrix chain with minimum cost. There are total (2n-2)!/n!*(n-1)! calculations in brute force method, which
can be proved that the number of operation is a catalan number. 

MCP is a classical dynamic problem, due to the subproblems are depended on other solved subproblems. If we memorize the solved
subproblems in a table, we just need to calculate each subproblem once. And there are n to the 2 (n2) subproblems, cost runtime 
n2. The extra run time is o(n), the overall runtime is o(n3).

The auxiliary table m[i,j] represent the smallest problem. 

Firstly, filling the table m with formula

m[i,j] = min(i <=k <=j) { m[i,k] + m[k+1, j] + p(i-1)*p(k)*p(j)}, where k is the position to partition the parentheses.

But how to fill the table m?

1. Initialize all the blank as "-".
2. Fill the main diagonal first, then the upper right diagonal, and then to the upper right, till to the end. 

Analysis process of MCP:
We want to find the last step that can achieve the minimum cost, suppose is A[i,k] * A[k+1,n], where k is the optimal partition
position.

How can we find the K????

Assume A[i,k] and A[k+1,n] are already the optimized subproblem. 

How can we get optimized A[i, k] and A[k+1, n]

We need scan through the matrix from i to j (0<= i < j <=n) to find the minimum one, which can be derived by the following formula

m[i,j] = min(i <=k <=j) { m[i,k] + m[k+1, j] + p(i-1)*p(k)*p(j)}, where k is the position to partition the parentheses, p is the
dimension of matrix.
"""
from pprint import pprint
def mcp(A):
	"""
	A is the list contains the dimensions of matrix(assume square matrix)
	S is a list to record the position of optimized partition
	"""
	length = len(A)
	n = length -1 # (length-1) number of product for the number of length matrix 

	row = ["-"]*(length)
	m = [0]*(length)
	

	for i in range(length):
		m[i] = row[:]
	
	pprint(m)
	print 

	for i in range(length):
		m[i][i] = (0,0)
	pprint(m)
	print 


	#L is the chain length (2,3,4,5)
	for L in range(2,length):
		for i in range(1,length-L+1):

			j = i + L -1
			MIN = float('inf')
			position = 0
			for k in range(i,j):
				q = m[i][k][0] + m[k+1][j][0] + A[i-1]*A[k]*A[j]

				if q < MIN:
					MIN = q
					position = k
			m[i][j] = (MIN,position)

	pprint(m)
	return m[1][length-1]


def main():
	A = [10,20,1,40,5,30,15]
	print mcp(A)

if __name__=="__main__":
	main()



























