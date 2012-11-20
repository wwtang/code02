"""
Bit manipulation
Given two 32 bit number N and M, insert M into N from index i to j, (suppose there is enough space in M to hold N)

ex: 
input M = 10011, N  = 10000000000, i = 2 ,j = 6
output N  10001001100


algorithm

1.Try to figure out a  bit number   1111110000011 as mark.


2. Perform N & mark to clear the substitute part (j, i)

3 . Perform M & N to achieve the target result 

"""

def substitute(N,M,i,j):

	mark = figureMark(i,j)

	newN = N & mark

	return M & newN 





def figureMark(i,j):
	"""
	(int, int) --> int

	i is the begin index 
	j is the end index 

	from right to left j > =i 
	"""

	temp = 1 << j+1
	temp1 = (temp -1)<<i
	#~((1 << j+1)-1)<<i
	return ~temp1 


def main():
	M = int('10000000000',2)
	N = int('10011',2)

	i = 2
	j = 6

	print substitute(N,M,i,j)

if __name__=="__main__":
	main()

