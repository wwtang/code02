"""
DFS in python
"""


graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph1 = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }            

graph2 = {
	
		'2' :['0','3'],
		'3' :['3'],
		'0' :['1','2'],
		'1'	:['2']
		}

def dfs(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path

	# if not graph.has_key(start):

	#  	return []

	for node in graph[start]:
		print "Node", node
		# if node exists in path, means the node goes back, there is no way to forward 
		path += dfs(graph, node, end, path)
		# 


			# if newPath: return newPath
	#return None 

	return path

def find_path(graph, start, end, path=[]):

	path = path + [start]
   	if start == end:
 	   return path
   	if not graph.has_key(start):
   		return None

   	for node in graph[start]:

   		if node not in path:

   			newpath = find_path(graph, node, end, path)

        	if newpath:
        		return newpath

   	return None


# def find_path(graph, start, end, path=[]):

# 	path = path + [start]
#   	if start == end:
#    		return path
#    	if not graph.has_key(start):
#    		return None
#     for node in graph[start]:

#      	if node not in path:
#         	newpath = find_path(graph, node, end, path)
#            	if newpath: return newpath
#     return None

print find_path(graph2,'2','3')
print find_path(graph1,'1','11')
#print dfs(graph1,'1','9')


# print dfs(graph,'B','D')
# print dfs(graph,'C','D')
# print dfs(graph,'E','D')