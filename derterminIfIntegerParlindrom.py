"""

Given a number determine whether it is a integer

"""

def reverserInt(n):
	rev = 0
	while n > 0:
		rev = rev*10 + n%10
		n /= 10

	return rev



def main():
	n = 123
	print reverserInt(n)

if __name__=="__main__":
	main()