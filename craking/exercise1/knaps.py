"""
0/1 knapsack (similar to coins)

"""
from pprint import pprint 

def knapsack(vl, wt, k):
	"""
	return a list of index, which can contribute to the maximum profits
	vl value
	wt weight 
	len(vl) == len(wt)
	k is the capacity of the knapsack 
	"""
	if len(vl) != len(wt):
		print "Invalid data"
		return None
	#initial table profit 
	length = len(vl)
	profit = [0]*(length+1)

	row = [0]*(k+1)

	for i in range(length+1):
		profit[i] = row[:]

	#track helper

	#table[i][j] = 0 when i ==0 or j ==0


	# fill profit column by column 
	for  j in range(k+1):
		for i in range(length+1):

			if i ==0 or j ==0:
				profit[i][j] =0

			elif j - wt[i-1] >=0:# wt[i-1] is the last element in wt
				profit[i][j] = max(vl[i-1] + profit[i-1][j-wt[i-1]], profit[i-1][j])
			else:
				profit[i][j] = profit[i-1][j]

	pprint(profit)
	return profit[length][k]


def main():
	wt = [5,4,3,2,4]
	vl = [4,2,4,1,5]
	k = 13

	print knapsack(vl, wt, k)

if __name__=="__main__":
	main()