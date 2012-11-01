graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def find_all_path1(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpath = find_all_path1(graph, node, end, path)
            print' newpath', newpath
            for newp in newpath:
                print "newp", newp
                paths.append(newp)
    return paths

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        print "find all the paths"
        return paths

def  find_shortest_path(graph, start, end, path=[]):
    path = path +[start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph,node,end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest= newpath
    return shortest

print find_path(graph, 'A', 'D')
print
print "*"*10
print

print find_all_path1(graph, "A", "D")
print
print "*"*10
print
print find_all_paths(graph,"A","D")

print
print "*"*10
print

print find_shortest_path(graph, "A","D")
