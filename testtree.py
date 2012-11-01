"""tree"""


class Node:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right = right

    def Insert(self,data):
        if data < self.data:
            if self.left is not None:
                self.left = Node(data)
            self.left.Insert(data)
        else:
            if self.right is not None:
                self.right = Node(data)
            self.right.Insert(data)

    def lookup(self, data, parent=None):
        if data = self.data:
            return self, None
        if data < self.data:
            self.left.lookup(data,self)
        else:
            self.right.lookup(data, self)

    def find_successor(self):
        successor = self.right
        while successor.left:
            successor = successor.left

    def count(self):
        
        count = 0
        if self.left is not None:
            count +=1
        if self.right is not None:
            count +=1

    def delete(self, data):
        c_num = self.count()
        node, parent = self.lookup(data)

        if c_num == 0:#no child
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            del node

        if c_num ==1:
            if node.left is not None:
                n = node.left
            else:
                n = node.right
            if parent.left is node:
                parent.left = n
            else:
                parent.right = n
       
        
        successor = self.find_successor()
        
        
        
