class Vertex:
    def __init__(self, data):
        self.data =data
        self.successor = []



#generate a Graph
def petersenGraph():
    v = [Vertex(i) for i in xrange(10)]
    edges = \
            [(0,1), (1,0), (1,2), (2,1), (2,3), (3,2), (3,4), (4,3), (4,0), (0,4),
          (5,6), (6,5), (6,7), (7,6), (7,8), (8,7), (8,9), (9,8), (9,5), (5,9),
          (5,0), (0,5), (6,2), (2,6), (7,4), (4,7), (8,1), (1,8), (9,3), (3,9)]
    for a, b in edges:
        v[a].successor.append(v[b])
    return v

def dfs(start, isGoal, result):
    if start in result:
        return False

    result.append(start)

    if isGoal(start):#reach the target item
        return True

    for s in start.successor:
        if dfs(s, isGoal, result):
            return True

    #NO path was found
    result.pop()
    return False

def main():
    v = petersenGraph()
    for vertex in v:
        print vertex.data
        print [item.data for item in vertex.successor]

    print "*"*20
    path = []

    if dfs(v[0], (lambda v: v.data ==7), path):
        print "Found path", [u.data for u in path]
    else:
        print "No path found"

if __name__=="__main__":
    main()
