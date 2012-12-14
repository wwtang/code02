"""

add an array with number 
"""

def add(n, num):
	arr = num2Arr(n)
	arr2 = num2Arr(num)

	if len(arr) == 0 and num ==0:
		return []

	if len(arr) ==0:
		return arr2

	if num == 0:
		return arr


	res = []
	carry = 0 

	i = len(arr)-1
	j = len(arr2)-1

	# while i>=0 and j>=0:

	# 	tmp = arr[i] + arr2[j] + carry
	# 	res.append(tmp%10)
	# 	carry = tmp/10
	# 	i -= 1
	# 	j -= 1

	# while i>=0:
	# 	tmp = arr[i] + carry

	# 	res.append(tmp%10)

	# 	carry =tmp/10
	# 	i -=1

	# while j>=0:
	# 	tmp = arr2[j] + carry

	# 	res.append(tmp%10)
	# 	carry = tmp/10
	# 	j -=1

	while i >= 0 or j>=0:

		tmp = carry

		if i >=0:
			tmp += arr[i]
			i -=1

		if j >=0:
			tmp +=arr2[j]
			j -=1

		res.append(tmp%10)
		carry = tmp/10


	if carry>0:
		res.append(carry)

	res.reverse()



	return arr2Num(res)


def num2Arr(num):
	"""
	helper function that used to convert the integer into array representation 
	"""
	helper = []

	while num>10:
		helper.append(num%10)
		num = num/10

	helper.append(num)

	helper.reverse()
	return helper

def arr2Num(arr):
	"""
	helper function that used to convert the array into integer, which is the reverse process of num2Arr
	"""
	if len(arr) == 0:
		return None

	num = 0

	for i in range(len(arr)-1):

		num = (num+arr[i])*10

	num += arr[len(arr)-1]

	return num
def main():
	arr = [1,5,4]
	num = 77
	# print add(arr,num)
	# print add([1,0,0], 0)
	# print add([9,9,9], 1)
	# print add([1], 9)
	# print add([1],99999999)
	print add(111111111111111,222222222222)



if __name__=="__main__":
	main()





