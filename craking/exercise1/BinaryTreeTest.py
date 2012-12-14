"""

1. build a binary tree with minimum height. 
2. produce the inOrder, preOrder and postOrder array of nodes.
3. find the lowest common ancestor of two nodes.
"""

#Node class:

class Node:

	def __init__(self, data, left =None, right = None, parent = None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def setLeft(self, node):
		self.left = node
		node.parent = self
       	# self.left.parent = self
   	def setRight(self, node):
   		self.right = node
       	self.right.parent = self


def buildMinBT(arr, first, last):
	"""
	Build a binary tree with minimum height
	good suggestion is start from the middle of the array, whose left child is the middle element of the left part, right child is
	the middle element of its right part. total height is log(N)
	"""
	if first > last:
		return None

	mid = (first+last)/2

	#root if the tree
	root = Node(arr[mid])

	left = buildMinBT(arr, first, mid -1)

	right = buildMinBT(arr, mid+1, last)

	root.setLeft(left)
	root.setRight(right)

	return root

def printTree(root):

	if not root:
		return None


	left = printTree(root.left)
	current =  root.data
	right = printTree(root.right)

	return [current, left ,right]

def inorderArray(root):
	if not root:
		return []
	res = []

	left = inorderArray(root.left)
	current = root.data
	right = inorderArray(root.right)

	res.extend(left)
	res.append(current)
	res.extend(right)

	return res

def preOrderArray(root):
	if not root:
		return []

	res = []
	current = root.data
	left = preOrderArray(root.left)
	right = preOrderArray(root.right)

	res.append(current)
	res.extend(left)
	res.extend(right)
	return res

def postOrderArray(root):
	if not root:
		return []

	res = []

	left = postOrderArray(root.left)
	right = postOrderArray(root.right)
	current = root.data

	res.extend(left)
	res.extend(right)
	res.append(current)
	return res
def lowestCommonAncestor(root,p,q):
	"""
	return the lowest common ancestor of node p and q.
	assume that the ancestor of root is root itself.
	"""
	if not root:
		return None
	#root is p or q
	if root.data == q.data or root.data ==p.data:
		return root

	L = lowestCommonAncestor(root.left, p, q)
	R = lowestCommonAncestor(root.right, p, q)

	if L and R:
		return root

	return L if L else R
	# 


def main():
	arr = [3,4,2,5,6,72,9,8]
	root = buildMinBT(arr, 0, len(arr)-1)
	print printTree(root)
	# print inorderArray(root)
	# print preOrderArray(root)
	# print postOrderArray(root)
	# p = Node(6)
	# q = Node(2)
	# print lowestCommonAncestor(root, p, q).data
	# print
	# print printTree(root)

if __name__=="__main__":
	main()
