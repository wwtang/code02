"""
make change

"""

def makeChange(cents, coins):
	res = []
	i = 0

	while cents:
		c, cents = divmod(cents, coins[i])
		i +=1

		
		if c:
			res.append(c)
		else:
			res.append(0)

	return res


def main():
	coins= [25,10,5,1]
	cents1 = 100
	# cents2 = 42
	# cents3 = 85
	# cent4 = 10
	# cents5 = 0
	# cents6 = 1

	print makeChange(cents1, coins)
# print makeChange(cents2, coins)
# print makeChange(cents3, coins)
# print makeChange(cent4, coins)
# print makechange(cent, coins)


if __name__=="__main__":
	main()