"""
Eight queens problem, 
In python there is no need to initialize an avari


"""

counter = 0
# def isValid(state,nextx):
# 	"""
# 	(list, int) --> boolean
# 	state is list to represent the state history of the queens, the length represent the current row.
# 	nextx is the position is the new row, from 0 to 8 
# 	return True, if conflict, else False
# 	"""

# 	nexty = len(state)

# 	for i in range(nexty):
# 		if abs(nextx-state[i]) in (0, nexty-i):
# 			return	True
# 	return False


# the ith row, kth col
def find(i,k,q):
	"""
	(int, int, list) -->boolean	
	i is the ith row
	k is the kth col
	q is a list
	"""

	j = 0
	while j <i:
		#if q[j] == k or (i-j) == abs(q[j]-k):
		#print "the current position is (%s, %s)"%(i,k)
		if abs(q[j] - k) in [0, i-j]:
			return False
		j +=1
	#print "The valid position is (%s, %s)"%()
	return True


def placeQ(r, n,q):

	"""

	r is the current row, n is the grid size.
	q is the state list 
	result is a list to hold valid path 

	"""

	#print "Current row is %s"%r
	if r == n:
		#print q 
		printOut(q)
				
	#traceback to the 0th row,
	else:
		for i in range(n):#for every position in row, 
			#print "Current checking position is (%s, %s)"%(r, i)
			if find(r,i,q):
				#print "Valid position (%s, %s)"%(r, i)
				q[r] = i
				#print "q is: %s" %q
				placeQ(r+1,n,q)



def printOut(chessboard):

	chess = []
	for x in range(len(chessboard)):
		row = []
		for y in range(len(chessboard)):
			if chessboard[x] == y:
				row.append("Q")
				#print "Q"
			else:
				#print "X"
				row.append("X")
		chess.append(row)
	global counter
	counter +=1	
	print "the %s solution" %counter
	print "------------------------"
	print 
	for r in chess:
		print r
	print 
	print "------------------------"
	
				
def main():
	n = 4 
	q= [None]*n
	#paths = placeQ(0,n,q)
	placeQ(0,n,q)

	

if __name__=="__main__":
	main()