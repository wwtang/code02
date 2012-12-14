"""

determine whether a string of parentheses like "(()))((" is valid

1, count the number of "("
2, the number of "(" always no less than the number of ")"

use one counter 
"""


def checkParen(pstr):
	if len(pstr) ==0 :
		return False

	counter = 0

	for p in pstr:
		if p =="(":
			counter +=1
		elif p == ")":
			counter -=1

			if counter < 0:
				return False

	if counter != 0:
		return False

	return True

def main():
	pstr = "((()))"
	pstr1 = "((()"
	pstr2 = ")()()()"
	pstr3 = "()()()"
	pstr4 = "("
	print checkParen(pstr)
	print checkParen(pstr1)
	print checkParen(pstr2)
	print checkParen(pstr3)
	print checkParen(pstr4)

if __name__=="__main__":
	main()


