"""node is the basic structure of tree
build it first
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #insert node

    def Insert(self, data):
        #new data is data, self data is the current data
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
                
    def Lookup(self, data, parent=None):

        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.Lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.Lookup(data,self)
        else:
            return self, parent


    def children_count(self):
        """return the number of children 0, ,1, 2"""
        if node is None:
            return None
        count = 0
        if self.left:
            count +=1
        if self.right:
            count +=1
        return count
            
