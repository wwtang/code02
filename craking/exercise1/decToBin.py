"""
2 -->10
3-->11
"""


def decToBin(num):
	if num ==0:
		return [0]

	res = []

	while num!=0:

		res.append(num%2)
		num /= 2


	res.reverse()

	return res

def decToHex(num):
	"""
	10 -->A 
	11 -->B 
	15 -->F
	"""

	hexDict = {1:1, 2:2, 3:3,4:4,5:5,6:6, 7:7, 8:8 , 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

	if num <10:
		return [num]

	res = []

	while num !=0:
		res.append(hexDict[num%16])
		num /= 16

	res.reverse()

	return res

def main():
	print decToBin(5)
	print decToBin(4)
	print decToBin(1)
	print decToBin(0)
	print decToBin(32)
	print decToHex(100)
	print decToHex(15)

if __name__=="__main__":
	main() 