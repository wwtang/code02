"""
Dynamic problem 
Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. Find the minimum number of coins the sum of which is S 
(we can use as many coins of one type as we want), or report that it's not possible
 to select coins in such a way that they sum up to S. 


 DP way is the bottom up manner, and you can also use top-down manner to figure it out

 DP pseudo code

 Initial the array Min[] with infinity 

 for sum =0 to S
 for j = 0 to N-1
 	if v[j] < sum and Min[sum-V[j]] + 1 < Min[sum]

 	Min[sum] = Min[sum-V[j]] + 1

 return Min[s]

"""

def makechange(sum, coins):
	Max = float('inf')
	table = [Max]*(sum+1)
	table[0] = 0
	trace = []

	for i in range(sum+1):
		last = 0
		for j in range(len(coins)):
			if coins[j] <= i and table[i-coins[j]] + 1 < table[i]:

				table[i] = table[i-coins[j]]+1
				last = coins[j]
		#print "sum is %s and last is %s" %(i, last)
		trace.append((last, i-last))

	print table
	print trace
	print printTrace(trace)
	return table[sum]

def printTrace(trace):
	"""
	list --> list
	trace --> [ coins]
	"""
	res = []

	Index = len(trace)-1

	res.append(trace[Index][0])
	nextIndex  = trace[Index][1]
	while nextIndex:
		res.append(trace[nextIndex][0])
		nextIndex  = trace[nextIndex][1]
	return res


def main():
	sum = 100
	coins = [1,5,10,25]

	res = makechange(sum, coins)
	print res

if __name__=="__main__":
	main()

