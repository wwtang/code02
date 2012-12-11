"""
common strategies to solve problems, divide and conquer, greedy, and dynamic programming.

first try divide and conquer. if there are many overlap subproblems, we can use DP to figure it out



"""
#recursive manner 
def count(s, m, n):

	if n==0:
		return 1

	if m ==0:
		return 0

	if n < 0:
		return 0

	if m <= 0 and n >= 1:
		return 0

	return count(s, m-1, n) + count(s, m, n-s[m-1])

# There are many overlapped subproblems here, you can figure it out by draw the 
#recursive tree. You can use DP to improve the efficiency.
def count2(s, m, n):
	table = [0]*(n+1)
	cols  = [0]*m

	# for row in table:
	# 	row = cols[:]

	for i in range(n+1):
		table[i] = cols[:]

	# print table
	for i in range(m):
		table[0][i] = 1

	for i in range(1, n+1):
		for j in range(m):

			# the last item included
			x = table[i-s[j]][j] if i >= s[j] else 0

			# the last item excluded
			y = table[i][j-1] if j >=1 else 0

			table[i][j] = x +y

	return table[n][m-1]


def count3(s, m,n):
	table = [0]*(n+1)

	table[0] = 1

	for i in range(m):
		for j in range(s[i],n+1):
			table[j] += table[j-s[i]]

	return table[n]

# top-down manner, 
def count4(n, denom):
	nextDenom = 0;

	if denom == 25:
		nextDenom = 10
	elif denom == 10:
		nextDenom =5
	elif denom == 5:
		nextDenom = 1
	else:
		return 1

	ways = 0
	for i in range(0,n+1, denom):
		ways += count4(n-i, nextDenom)

	return ways


def main():
	s= [1,5,10,25]
	m = len(s)
	n = 100
	ways = count(s, m,n)
	print ways
	ways2 = count2(s, m, n)
	print ways2
	ways3 = count3(s,m,n)
	print ways3

	ways4 = count4(n, 25)
	print ways4



if __name__=="__main__":
	main()