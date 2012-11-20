"""
find all the subset of a set
"""


def finaSubset(str):
	if len(str)< 1:
		return None

	if len(str) ==1:
		return ["", str[0]]

	return finaSubset(str[:-1]) + newset(str)


def newset(str):
	news = []
	for s in finaSubset(str[:-1]):

		news.append(s + str[-1])

	return news 

def main():
	str ="abcd"


	print finaSubset(str)

if __name__=="__main__":
	main()
