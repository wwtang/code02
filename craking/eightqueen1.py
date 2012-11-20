"""
eight queens problem

from rookies to professional 


place queen on chessboard is the process to the locate the valid column

"""


# def confilct(state, nextx):
# 	nexty = len(state)
# 	for i in range(nexty):
# 		if abs(state[i] - nexty) in [0, nexty-i]:
# 			return True
# 	return False


# def queens(number, state):
# 	if len(state) == number -1:
# 		for pos in range(number):
# 			if not confilct(state, pos):
# 				yield pos
# 	else:



# def main():
# 	result =  list(queens(4))
# 	for r in result:
# 		print r
# if __name__=="__main__":
# 	main()


# def confilt(colums, row1, col1):
# 	for i in range(col1):
# 		colum2 = colums[i]

def conflict(state,nextx):
	"""
	(list, int) --> boolean
	state is list to represent the state history of the queens, the length represent the current row.
	nextx is the position is the new row, from 0 to 8 
	return True, if conflict, else False
	"""

	nexty = len(state)

	for i in range(nexty):
		if abs(nextx-state[i]) in (0, nexty-i):
			return	True
	return False




def placeQueens(num, state):
	"""
	(int, list) -->list
	num is the number of queens will be placed in the chessboard.
	state is the history of queens on the chessboard.
	return the position of the rest of queens .

	"""
	if len(state) == num-1:
		for pos in range(num):
			if not conflict(state, pos):
				yield pos 



def  queens(num = 8, state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num -1:
				yield (pos,)
			else:
				for result in queens(num, state+(pos,)):
					yield(pos,) +result


					

def  queens1(num = 8, state=[]):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num -1:
				yield [pos]
			else:
				for result in queens1(num, state+[pos]):
					yield[pos] +result
















