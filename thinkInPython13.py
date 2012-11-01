"""

histogram
"""
import string

def histogram(seq):
	d = {}
	for item in seq:
		if item not in d:
			d[item] = 1
		else:
			d[item] +=1
	return d


def histogramPortion(seq):
	#portionDict = {}
	length = len(seq)

	d = histogram(seq)

	for k, v in d.items():
		
		d[k] = str(v)+ "/" + str(length)
	return d

def removePunc(str):
	

def main():
	seq = "abcdac"
	print histogram(seq)
	print histogramPortion(seq)

if __name__=="__main__":
	main()