"""
remove punctuation

"""


import string

def removePunc(str):
	lst = list(str)
	for c in lst:
		if c in string.punctuation:
			lst.remove(c)
			print c
	return "".join(lst).strip() 


def main():
	str = " To do this, you can override these class attributes:"
	print removePunc(str)


if __name__=="__main__":
	main()