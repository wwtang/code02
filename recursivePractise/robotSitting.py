"""
A robot sitting on the left  top of the M*N grid

"""

#find all the possible way without obstacle

def allPath(n,m):
	if n ==0 or m == 0:
		return 1
	else:

		print (n, m) 

		return allPath(n-1,m)+allPath(n,m-1)


def printPath(n,m,path):

	totalPath = []
	paths = []
	
	if n == 0:
		for i in range(m):
			path  =  path + " down ->" 

		totalPath.append(path)
		paths.append(totalPath)
		print totalPath

		#print [path]
		

	elif m ==0:
		for i in range(n):
			path =  path + " left ->" 
		#print path
		totalPath.append(path)
		paths.append(totalPath)
		print totalPath


	else:
		printPath(n-1,m, path + " left ->")
		printPath(n,m-1, path + " down ->")

	return paths

def allPathWithObstacle(n,m,obs):
	if (n,m) in obs:
		return 0
	if n ==0 or m==0:
		return 1
	return allPathWithObstacle(n-1,m,obs) + allPathWithObstacle(n,m-1, obs)



# def printAllPath(n,m,obs,path):
# 	if (n,m) in obs:
# 		return None

# 	else:
# 		if n==0:
# 			for i in range(m):
# 				if obstacle[m]:
# 					path = " down " + path
# 				print path
# 		elif m ==0:
# 			for i in range(n):
# 				path = " right "+ path
# 				print path
# 		else:
# 			printAllPath(n-1,m,obs, " down " + path)
# 			printAllPath(n,m-1,obs, " right " + path)


def main():
	# print allPath(3,3)
	paths = printPath(3,3," ")
	print paths, len(paths)
	# obstacle = [(3,2),(1,1)]
	# print allPathWithObstacle(3,3,obstacle)
	# printAllPath(3,3,obstacle,"")

if __name__=="__main__":
	main()