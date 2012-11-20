"""
Implement bfs in python


"""

graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue, path is a list, 
        path = queue.pop(0)
        # print"path, %s"%path
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue, create a new path with each of its child
        for adjacent in graph.get(node, []):
        	print "path is %s"%path
           	new_path = list(path)
           	print "The raw path is %s" %new_path
	        new_path.append(adjacent)
           	print"new_path %s"%new_path
           	# print
           	# print "Before enqueue, the queue is %s"%queue
           	queue.append(new_path)
           	# print "after enqueue, the enqueue is %s "% queue
           	# print

def traceBack(parent, start, end):
	path = [end]
	while path[-1] != start:
		path.append(parent[path[-1]])
	path.reverse()
	return path

def bfs1(graph, start, end):
	parent = {}
	Q = [start]
	while Q:
		node = Q.pop(0)

		if node == end:
			return traceBack(parent, start, end)

		for adj in graph.get(node, []):
			Q.append(adj)
			parent[adj]  = node
			print parent






def main():
	print bfs1(graph, '1', '11')

if __name__=="__main__":
	main()