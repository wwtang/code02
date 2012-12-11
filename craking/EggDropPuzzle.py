"""
eggDrop puzzle.  http://www.geeksforgeeks.org/archives/18812

Question description on book:

There is building of 100 floors. If an egg drops from the Nth floor or above, it will break
. If it's dropped from any floor below, it will not break. You're given tow eggs. Find
N, while minimizing the number of drops for the worse case;

First of all you need to understand the question, " minimizing the number of worse case"

so what's worse case?
list all the worse case and find the minimum one ?

if we only have one egg, what can we do to find the right N? the best way is drop from the
first floor if the egg not break, then raise the floor by one, until to the end. So the
worse case here is 100. 
How about 2 eggs?

Well, this problem is not actually to find the critical floor, but merely to decide floor
from which eggs should be dropped so that the total number of trails will be minimized 

"""

#recursive version
from pprint import pprint 

def eggDrop(n,k):
	"""
	int, int --> int

	n is the number of eggs
	k is the number of floors


	"""
	#  one floor or zero floor
	if k==1 or k==0:
		return k 

	# only one egg, we need to try to drop from each floor 
	if n == 1:
		return k

	Min = float('inf') 
	res = 0

	for x in range(1,k):
		#res is the worse case
		res =  Max(eggDrop(n-1, x-1), eggDrop(n, k-x))
		if res < Min:
			Min  = res

	return Min +1

def Max(a ,b ):
	return a if a>b else b


def eggDrop2(n,k):
	"""
	DP version 


	"""
	inf = float('inf')

	table = [0]*(n+1)
	cols = [0]*(k+1)

	#initial the table
	for i in range(n+1):
		table[i] = cols[:]

	# 0 floor need no trail, 1 floor try it once
	for i in range(n+1):
		table[i][0] = 0
		table[i][1] = 1

	# if only one egg, we need to try the floor one by one
	for j in range(k+1):
		table[1][k] = k

	


	for i in range(2, n+1):
		for j in range(2, k+1):
			table[i][j] = inf
			for x in range(2, j):
				res =1+ Max(eggDrop2(i-1, x-1), eggDrop2(i, j-x))
				if res < table[i][j]:
					table[i][j] = res

	#pprint(table)
	return table[n][k]



def main():
	k = 100
	n = 2
	#print eggDrop(n,k)
	print eggDrop2(n,k)

if __name__=="__main__":
	main()
