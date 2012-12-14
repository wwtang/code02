"""
lowest common ancestor 
three method 

"""

class Node:
	def __init__(self, data, left=None, right=None):
		self.data=data
		self.right = right
		self.left = left

	def __eq__(self, other):
		
		return True if self.data == other.data else False


def nodeCover(root, node):
	if not root:
		return False
	if root == node:
		return True
	L = nodeCover(root.left, node)
	R = nodeCover(root.right, node)

	return L or R

def LCA(root, p, q):
	"""
	if p is in subtree of q or p is the child of q, then q is their lowest common ancestor, and vice versa.
	"""

	if not root:
		return None 

	if not nodeCover(root,p) or not nodeCover(root, q):
		return None

	pInLeftTree = nodeCover(root.left, p)
	qInLeftTree = nodeCover(root.left, q)

	#if p and q on the left and right side of root, root is their lca 
	if pInLeftTree != qInLeftTree:
		return root

	# p, q on the same side of root 
	childNode = root.left if pInLeftTree else root.right

	return LCA(childNode, p, q)

def printTree(root):
	if not root:
		return None

	L = printTree(root.left)
	R = printTree(root.right)

	return [root.data, L, R]

def inorderArr(root):
	if not root:
		return[]
	res = []
	left = inorderArr(root.left)
	current = root.data
	right = inorderArr(root.right)
	res.extend(left)
	res.append(current)
	res.extend(right)
	return res

def preorderArr(root):
	if not root:
		return []

	res = []

	current = root.data
	left = preorderArr(root.left)
	right = preorderArr(root.right)

	res.append(current)
	res.extend(left)
	res.extend(right)

	return res

def postorderArr(root):
	if not root:
		return []

	res = []


	left = postorderArr(root.left)
	right = postorderArr(root.right)
	current = root.data

	res.extend(left)
	res.extend(right)
	res.append(current)

	return res

def main():
	root = Node(5)
	n1 = Node(4)
	n2 = Node(6)
	n3 = Node(3)
	n4= Node(1)
	n5 = Node(7)
	n6 = Node(8)
	root.left = n1
	root.right = n2
	n1.left =n3
	n1.right = n4
	n2.left = n5
	n2.right = n6
	print printTree(root)
	print LCA(root, n5, n6).data
	print "inorder", inorderArr(root)
	print"preorder", preorderArr(root)
	print "postorder", postorderArr(root)


if __name__=="__main__":
	main()



