"""

add an array with number 
"""

def add(arr, num):
	arr2 = num2Arr(num)

	if len(arr) == 0 and num ==0:
		return []

	if len(arr) ==0:
		return arr2

	if num == 0:
		return arr


	res = []
	carry = 0 

	i = len(arr1)-1
	j = len(arr2)-1

	while i>=0 and j>=0:

		tmp = arr1[i] + arr2[j] + carry
		res.append(tmp%10)
		carry /= 10
		i -= 1
		j -= 1

	while i>=0:
		tmp = arr1[i] + carry
		res.append(tmp%10)
		carry /= 10

	while j>=0:
		tmp = arr2[j] + carry
		res.append(tmp%10)
		carry /= 10

	if carry>0:
		res.append(carry)

	res.reverse():

	return res


def num2Arr(num):
	helper = []

	while num>10:
		helper.append(num%10)
		num = num/10

	helper.append(num)

	helper.reverse()
	return helper

def main():
	arr = [1,3,4]
	num = 77
	print add(arr,num)

if __name__=="__main__":
	main()





