"""
Floyd Walshall shortest path algorithm 

first convert the graph into adjacent matrix
than apply the FloydWalshall Algorithm 

"""
from pprint import pprint
def adj(g):
	"""
	convert the graph into adjacent matrix
	>>> g = {1: {2: 3, 3: 8, 5: -4}, 2: {4: 1, 5: 7}, 3: {2: 4}, 4: {1: 2, 3: -5}, 5: {4: 6}}
    >>> adj(g)
    {1: {1: 0, 2: 3, 3: 8, 4: inf, 5: -4}, 2: {1: inf, 2: 0, 3: inf, 4: 1, 5: 7}, 3: {1: inf, 2: 4, 3: 0, 4: inf, 5: inf}, 4: {1: 2, 2: inf, 3: -5, 4: 0, 5: inf}, 5: {1: inf, 2: inf, 3: inf, 4: 6, 5: 0}}
	"""

	inf = float('inf')
	vertices = g.keys()

	dist = {}
	for i in vertices:
		dist[i] = {}
		for j in vertices:
			try:
				dist[i][j] = g[i][j]

			except KeyError:
				if i==j:
					dist[i][j] =0
				else:
					dist[i][j] = inf
	return dist


def fw(dist):
	"""
	apply floyd walshall algorithm to dist
	>>> g = {1: {2: 3, 3: 8, 5: -4}, 2: {4: 1, 5: 7}, 3: {2: 4}, 4: {1: 2, 3: -5}, 5: {4: 6}}
    >>> fw(adj(g))
    {1: {1: 0, 2: 1, 3: -3, 4: 2, 5: -4}, 2: {1: 3, 2: 0, 3: -4, 4: 1, 5: -1}, 3: {1: 7, 2: 4, 3: 0, 4: 5, 5: 3}, 4: {1: 2, 2: -1, 3: -5, 4: 0, 5: -2}, 5: {1: 8, 2: 5, 3: 1, 4: 6, 5: 0}}
	"""
	#res = dict(dist)
	vertices = dist.keys()
	res = dict(dist)
	for i in vertices:
		for j in vertices:
			for k in vertices:
				
				res[i][j] =  min(res[i][k]+res[k][j], res[i][j])

	return res

def main():
	g = {1: {2: 3, 3: 8, 5: -4}, 2: {4: 1, 5: 7}, 3: {2: 4}, 4: {1: 2, 3: -5}, 5: {4: 6}}
	g1 = {
	'0':{'1':5,'3':10},
	'1':{'2':3},
	'2':{'3':1},
	'3':{}
	}	
	pprint(adj(g))
	#pprint(fw(adj(g)))

if __name__=="__main__":
	main()
	import doctest
	doctest.testmod()




