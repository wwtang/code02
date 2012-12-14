"""
0/1 knapsack problem on book
dynamic programming 

input list of tuple data = [(5,4),(4,2),(3,4),(2,1),(4,5)], k = 13
index represent the item number, ex (5,4) is the first item, (4,5 ) is the 5th item.
first element in each tuple is the weight of item, ex for (5,4) 5 is the weight and the 4 is price.
k is the total capacity of the knapsack. The total weight of all items that placed in the knapsack can't exceed k.


Goal:
Place the item in the item list into knapsack so that the total profit is maximum, with the limitation that the total weight of
items can not over the capacity of the knapsack.


Output: a list of items that can maximum the profit


There are two helper array in this problem profit[i][j] and d[i][j].
profit[i][j] means the maximum profit that can be achieved at the ith item with the remaining knapsack capacity j. To fill this
array there total rum time is n*k.

profit[i][j] = {
				0   				if i = 0;
				0 					if j = 0;
				profit[i-1][j] 		if w[i] > j; can't not place the current item into knapsack;
				
				max(profit[i-1][j], if w[i] < j; place the ith item into knapsack;
				p[i] + profit[i-1][j-w[i]])  
	
				}


d[i][j] is used to record which item has been put into knapsack. If the current item has been selected mark as 2, else 1

d[i][j] = {
	
		1 		if ith item is not  placed into knapsack;
		2 		if ith item is placed into knapsack;
}	


And we need a print function to print out the selected items. From the end to the beginning.

j = k
for i in range(n,-1,-1):
	print d[i][j]: if d[i][j] == 2:
		j = j-w[i]


"""

from pprint import pprint 

def knapsack(data, k):
	if k < 0:
		return None

	#initial the table profit	
	n = len(data)

	kp = [0]*(k+1)
	profit = [0]*(n+1)
	#d is the track
	d = [0]*(n+1)

	#create the table
	for i in range(n+1):
		profit[i] = kp[:]
		d[i] = kp[:]


	data.insert(0,(0,0))
	#fill the array
	for j in range(k+1):
		for i in range(n+1):

			if i == 0 or j ==  0:
				profit[i][j] = 0
				d[i][j] = 0

			elif data[i][0] > j:
				profit[i][j] = profit[i-1][j]
				#d[i][j] = 1

			elif data[i][0] <=j:
				Max = profit[i-1][j]

				NewItem = data[i][1] + profit[i-1][j-data[i][0]]

				if NewItem > Max:
					profit[i][j] = NewItem
					
					d[i][j] = 2
				else:
					profit[i][j] = Max 

					d[i][j] = 1

	
	pprint(profit)



	print 


	pprint(d)

	res = []			 
	j = k
	for i in range(n,-1,-1):
		if d[i][j] == 2:
			res.append(data[i])
			j = j - data[i][0]



	
	return res 



def main():
	data = [(5,4),(4,2),(3,4),(2,1),(4,5)]
	k = 13

	print knapsack(data,k)


if __name__=="__main__":
	main()


