"""

Given a sorted array, create a binary search tree with minimum height
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.left =None
		self.right = None


def buildMinBST(arr, start, end):
	if start > end:
		return None

	mid = (start+end)/2

	root = Node(arr[mid])

	root.left = buildMinBST(arr, start, mid-1)
	root.right = buildMinBST(arr, mid+1, end)
	return root

def printTree(root):
	
	if not root:
		return None

	return[root.data, printTree(root.left), printTree(root.right)]

def maxHeight(tree):
	# height = 0
	# while tree.left or tree.right:
	# 	height +=1
	# 	tree = tree.left if tree.left else tree.right
	# return height

	if not tree:
		return 0

	return 1+ max(maxHeight(tree.left), maxHeight(tree.right))

def collectInoder(tree):
	res = []
	res.append(inorder(tree))
	return res 

def inorder(tree):

	res = []
	left = None
	right = None
	current  = None

	if tree == None:
		return []
	
	else:
		left = inorder(tree.left)
		current = tree.data
		right = inorder(tree.right)

	res.extend(left)
	res.append(current)
	res.extend(right)
	return res

def postOrder(tree):
	res = []
	right = None
	left = None
	current = None

	if tree == None:
		return []
	else:
		left = postOrder(tree.left)
		right = postOrder(tree.right)
		current = tree.data

	res.extend(left)
	res.extend(right)
	res.append(current)
	return res

def preOrder(tree):
	res = []
	right = None
	left = None
	current	 = None

	if tree == None:
		return []

	else:
		current = tree.data
		left = postOrder(tree.left)
		right = postOrder(tree.right)

	res.append(current)
	res.extend(left)
	res.extend(right)
	return res
def main():
	arr = [1,2,3,4,5,6,7,8,9]
	start = 0
	end = len(arr)-1

	tree = buildMinBST(arr, start, end)

	# print tree.data, tree.left.data, tree.right.data
	# print printTree(tree)
	# print maxHeight(tree)
	# print maxHeight(tree.left), maxHeight(tree.right)
	# print collectInoder(tree)
	#print postOrder(tree)
	print inorder(tree)
	print postOrder(tree)
	print preOrder(tree)
if __name__=="__main__":
	main()