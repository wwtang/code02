def count_letters(sen):
	res = {}
	for c in sen:
		res.setdefault(c,0)
		res[c] +=1

	return res


def count_letters1(sen):
	res = {}
	for c in sen:
		if c not in res:
			res[c] = 1
		else:
			res[c] +=1
	return res


def main():
	arr = 'asjhfdjahchajsdhfkasdjkfhjasdf'
	print count_letters(arr)
	print
	print count_letters1(arr)
if __name__=="__main__":
	main()