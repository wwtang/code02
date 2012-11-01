"""use a list as queue"""

graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def bfs(graph, start, end):
    queue= []
    queue.append([start])#the source

    while queue:

        path = queue.pop(0) # path is a collection of list element

        node = path[-1]# markd the node's adjacent element as grey

        if node == end: #if reach the end, here to return the path
            return path

        for adjacent in graph.get(node,[]):# reach the adjacent element of node
            
            new_path = list(path)#make the previous path into a list, for the convinence to append next path node
            
            new_path.append(adjacent)#append the new path node to list
            queue.append(new_path)# equal to mark the adjacent as gray, list of list

def backtrace(parent, start, end):
    path = [end]
    while path[-1] !=start:
        #here append function  updates the path
        path.append(parent[path[-1]])# find parent reversely
    path.reverse()
    return path


def bfs1(graph, start, end):
    parent = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node ==  end:
            print "parent", parent
            return backtrace(parent, start, end)
        for adjacent in graph.get(node,[]):
            parent[adjacent] = node
            queue.append(adjacent)

def find_path(graph, start, end, path=[]):
    path =path +[start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return None
    for node in graph([start]):
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None








print bfs(graph, '1','11')
print bfs(graph,"1","12")
print bfs(graph,"5","12")
print
print "*"*10
print
print bfs1(graph, '1','11')
print bfs1(graph,"1","12")
print bfs1(graph,"5","12")
print
print "*"*10
print
print find_path(graph, "1", "11")

