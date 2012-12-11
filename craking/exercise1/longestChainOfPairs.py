"""
Longest chain of Pairs
"""

def LCP(pairs):

	length = len(pairs)
	pairs.sort()
	if length <2:
		return length

	table = [1]*length

	for i in range(length):
		for j in range(in):
			if pairs[i][0] > pairs[j][1] and table[i] < table[j] +1:
				table[i] = table[j] +1


	return table


def main():
	pairs = [(15,24),(39,64),(15,28),(27,40),(50,90)]

	print LCP(pairs)

if __name__=="__main__":
	main()