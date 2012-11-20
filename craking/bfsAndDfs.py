"""
DFS and BFS in python
"""
def printTime(func):
	import time
	def wrapper(*args):
		startTime = time.clock()
		ex = func(*args)
		endTime = time.clock()
		print"the run time for %s is %s "%(func.__name__, (endTime-startTime)*1000) 
		return  ex

	return wrapper

def traceBack(parent, root, target):
	"""
	(dict, node, node ) --> list 
	print out the path of bfs 
	"""
	path = [target]
	while path[-1] 	!= root:
		#trace back and reach the root 
		cn = path[-1]
		path.append(parent[cn])
	path.reverse()
	return path

@printTime
def bfs(graph, root, target):
	"""
	(graph, )
	Q : utilize a list as queue
	"""
	Q = [root]
	parent = {}

	# if not graph.has_key(root):
	# 	return None
	while Q:
		cn = Q.pop(0)

		if cn == target:
			return traceBack(parent, root, target)
		#check the children, pay attention to the leaf node 
		for adj in graph.get(cn,[]):
			Q.append(adj)
			parent[adj] = cn

@printTime
def dfs1(graph, root, end):
	return dfs(graph,root,end)

def dfs(graph, root, end, path = []):

	path = path + [root]

	if root == end:
		return path

	if not graph.has_key(root):
		return None

	for adj in graph[root]:
		if adj not in path:
			newpath = dfs(graph, adj, end, path)
			if newpath: return newpath
	return None	


def main():

	graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

   	root = '1'
   	target = '11'

   	print bfs(graph,root, target)
   	print
   	print dfs1(graph,root,target)


   	print bfs(graph,'1', '4')
   	print
   	print dfs1(graph,'1','4')

if __name__=="__main__":
	main()





