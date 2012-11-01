"""find successor"""


class Node:
	def __init__(self,  data):
		self.left= None
		self.right = None
		self.data = data
		
	def Insert(self,data):
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.Insert(data)
		else:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.Insert(data)
				
	def lookup(self, data, parent=None):
		if data == self.data:
			return self, None
		if data < self.data:
			if self.left is None:
				return None, None
			else:
				self.left.lookup(data, self)
		else:
			if self.right is None:
				return None, None
			else:
				self.right.lookup(data, self)
	
	def find_successor(self):
		successor = self.right
		while successor.left:
			successor = successor.left
		return successor
		
def main():
    a = [3,10,1,6,4,7,14,13]
    root = Node(8)
    for i in a:
        root.Insert(i)
        
    root.find_successor()


if __name__=="__main__":
        main()
    
