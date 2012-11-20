"""

Print all the parentheses without duplicates

"""

def printParen(n):
	"""
	n is the number of pairs of parentheses
	"""
	if n < 1:
		return []
	temp  =[0]*2*n
	res = []
	printParenthese(n,n,0,temp,res)

	print "res ",res
	return res


def pprintParen(n):
	lst = printParen(n)

	res = []
	for plist in lst:
		res.append("".join(plist))
	return res


def printParenthese(lcount, rcount, index ,temp,res):

	if lcount < 0 or rcount < lcount:
		return None
	if lcount== 0 and rcount == 0:
		# be careful here, everything point to temp, so temp change, all the variable that referred here will be changed 
		#be careful, copy the value of temp to a new container.
		wellFormat = temp[:]
		print "well formate temp", temp
		res.append(wellFormat)
		#print "res is",
		print "res appending the well format temp result",res

	if lcount > 0:
		temp[index] = '('
		print "temp left", temp
		#print temp
		printParenthese(lcount-1, rcount, index+1 ,temp,res)


	if rcount > lcount:
		temp[index] = ')'
		print "temp, right", temp
		#print "on the right side, ", temp		
		printParenthese(lcount, rcount-1, index+1 ,temp,res)
def main():
	print pprintParen(3)

if __name__=="__main__":
	main()