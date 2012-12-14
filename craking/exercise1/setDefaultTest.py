
def histogram(arr):
	res = {}

	for item in arr:
		res.setdefault(item,0)
		res[item] +=1

	return res



def main():
	arr = "asjhdfkjhaskdjfhkajshfd"
	str1 = [1,2,3,4,1,2,3,4,5,6,7,3,4,5,2,3,5,6,7,8,8]
	print histogram(arr)
	print histogram(str1)

if __name__=="__main__":
	main()