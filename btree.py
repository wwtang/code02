""" tree"""

class Node:
    def __init__(self, left=None, right=None,data=None):
        self.left = left
        self.right = right
        self.data = data

class Btree:
    def __init__(self):
        self.root = None

    def create(self, root):
        self.root.data  = raw_input("Enter data, '*' means empty: " )
        if self.root.data == "*":
            return
        self.root.left = Node()
        self.root.right = Node()
        self.create(self.root.left)
        self.create(self.root.right)

    def maketree(self, data):
        self.root = Node(data)
    def PreOrder(self):
        if self.root is not None:
            if self.root.data != "*":
                print self.root.data
                self.root.left.PreOrder()
                self.root.right.PreOrder()


if __name__ =="__main__":
    r = Btree()
    ra = Btree()
    ra.maketree(2)
