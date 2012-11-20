"""
Given an infinite number of quarters, dimes, nickels, cents. Write a method to calculate the number of ways to represent n cents 

This is a reduced style recursive problem. The base case is the fully reduced statement. 
ex makeChange(50 using 0 quarters, 5 dimes) is fully reduced to 1, since 5 dimes equals 50 cents
"""

def makeChange(n, demo):
	# if n < 1:
	# 	return None

	# if demo not in [25,10,5,1]:
	# 	print "No such coins"
	# 	return None 

	nextDemo = 0

	if demo == 25:
		nextDemo = 10

	elif demo == 10:
		nextDemo = 5

			
	elif demo == 5:
		nextDemo = 1

	elif demo == 1:
		return 1 


	ways = 0 

	#range(0, 100, 25) will generate 0, 25,50,75 No 100 
	for i in range(0, n+1, demo):
		ways += makeChange((n-i)*demo, nextDemo)

	return ways


def main():
	print makeChange(100,25)
	print makeChange(10,10)
	print makeChange(2,1)
	print makeChange(5,5)
	print makeChange(5,4)

if __name__=="__main__":
	main()

