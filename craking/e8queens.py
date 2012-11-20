"""
eight queens problem

This is a back trace problem, the difference between back trace and recursive is that there is an if-else determine condition 
before further recursive

chess grid representation: list or tuple which index represent each row and the value on each position means the columns position 

helper function: isValid which is used to determine if the current position is violate the rules

result: result is a list of state

algorithm:
begin form the first row, place the queen at the first valid row, then next, until to the last row. Then this is the first result 
and add the result to the final result 
"""



def placeQueen(row, columns,GRID_SIZE):
	"""
	row starts from 0 
	columns represent the states which is a list
	result is a list of list 
	"""
	result = []
	if row == GRID_SIZE-1:
		result.append(columns)

	else:
		for col in range(GRID_SIZE):
			if isValid(columns,row,col):
				columns[row] = col
				print 
				print "for the first row:%s the columns is:%s "%(row, columns)
				print 
				placeQueen(row+1, columns,GRID_SIZE)
				columns[row] = "*"
	return result


def isValid(columns, row, col):
	currentCol = col
	currentRow = row

	#for row ex the current row, check the validity 
	for exRow in range(row):
		if abs(exRow-row) in [0, abs(columns[exRow] - col)]:
			return False
	return True


def main():
	GRID_SIZE = 4

	columns = ["*"]*GRID_SIZE
	print placeQueen(0,columns,GRID_SIZE)

if __name__=="__main__":
	main()







