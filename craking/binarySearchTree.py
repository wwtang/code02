"""
Binary search tree in python 

attributes: left, right, data
methods:
insert
lookup return (data and parent)
nodeCount
delete
compare
print 

"""
class node(object):
	def __init__(self,data=None):
		self.left = None
		self.right = None
		self.data = data


	def insert(self,data):
		"""
		insert node with data into tree
		"""
		if data > self.data:
			if self.right is None:
				self.right = node(data) 
			else:
				self.right.insert(data)
		else:
			if self.left is None:
				self.left = node(data)
			else:
				self.left.insert(data)
	def insertNodes(self,lst):
		"""
		insert the data in list into tree
		"""
		for data in lst:
			insert(self,data)


	def lookup(self, target, parent = None):
		"""
		Find the target data, return its data and parent
		"""
		if target > self.data:
			if self.right is None:
				return None,None
			return self.right.lookup(target, self)
		elif target < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(target, self)
		return self.data, parent


	def childrenCounter(self):
		"""
		return the number of children of a node 
		"""
		ct = 0
		if self.left:
			ct +=1
		if self.right:
			ct +=1
		return ct 

	def delete(self, target):
		"""
		three scenarios: no child, one child, two children 

		"""
		node, parent = lookup(target)
		#no child
		if childrenCounter() ==0:			
			if parent.left == node:
				parent.left = None
			else:
				parent.right = None

		elif childrenCounter() == 1:
			if parent.left == node:
				if node.left:
					parent.left = node.left
				else:
					parent.left = node.right
			else:
				if node.left:
					parent.right = node.left
				else:
					parent.right = node.right

		else:
			if parent.left == node:
				parent.left = node.right
				node.right.left = node.left
			else:
				parent.right = node.left
				node.left.right = node.right

		del node 

	def compare(self, other):
		if other is None:
			return False
		if self.data != other.data:
			return False
		res = True

		if self.left is None:
			if other.left:
				return False
		else:
			res = compare(self.left, other.left)

		if self.right is None:
			if other.right:
				return False
		else:
			res = compare(self.right, other.right)
		return res 

	def printPreOrder(self):
		if self.left: self.left.printPreOrder()
		print self.data
		if self.right: self.right.printPreOrder()

	def printInOrder(self):
		print self.data
		if self.left: self.left.printPreOrder()
		if self.right: self.right.printPreOrder()

	def printPostOrder(self):
		if self.left: self.left.printPreOrder()
		if self.right: self.right.printPreOrder()
		print self.data

	def maxDepth(self):
		"""
		return the max depth of a tree 
		"""
		if self is None:
			return None
		lMax = self.left.maxDepth()
		rMax = self.right.maxDepth()

		return max(lMax,rMax)+1

	def size(self):
		if self.data is None:
			return 0
		else:
			return self.left.size() + 1 +self.right.size()

	def leftSize(self):
		if self.data is None:
			return 0
		return self.left.size()

	def getRank(self, d):
		if self.data == d:
			return self.leftSize
		elif self.data > d:
			if self.left is None:
				return None
			else:
				return self.left.getRank(d)
		else:
			rightRank = None if self.right is None else self.right.getRank(d)
			if rightRank is None:
				return None
			else:
				return self.left.size() + 1 +self.right.getRank(d)









