"""

Binary Tree Test
"""

class Node:
	left =None
	right = None
	data = 0
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None 
		self.parent = None

	def insertLeft(self, node):
		self.left = node

	def insertRight(self, node):
		self.right = node

def printTree(node):
	while node.left or node.right:
		print node.data
		node = node.left

def main():
	root = Node(9)
	node1 = Node(4)
	node2 = Node(3)
	node3 = Node(5)
	node4 = Node(7)

	root.insertLeft(node4)
	root.insertRight(node3)
	node4.insertLeft(node2)
	node4.insertRight(node1)

	print root.data
	printTree(root)

if __name__=="__main__":
	main()