

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def Insert(self, data):
        if data < self.data:#insert left
            if self.left is None:
                self.left = Node(data)
            else:#insert at left left recursively
                self.left.Insert(data)
        else:#Insert right 
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.Insert(data)
                
            
    def lookup(self,data,parent=None):#return node and its paretn, the default parent is None
     
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data,self)
        else:#default paretn is None, so if find the root, the parent is None, cool
            return self, parent

    def count(self):
        
        if self is None:
            return None
        count = 0
        if self.left:
            count +=1
        if self.right:
            count +=1
        return count
    # delete has three basic situation, leaf node, node with one child and node with two children
    def delete(self,data):
        node, paretn = self.lookup(data)
        c_num = self.count()

        
        # leaf node
        if c_num == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            del node

        #node with one child
        elif c_num == 1:
            if parent.left is node: # determin the left 
                if node.left:
                    parent.left = node.left
                else:
                    parent.left = node.right
            else:
                if node.left:
                    parent.right = node.left
                else:
                    parent.right = node.right
            del node

        
        #for node with two children, find the node.right  the left most child to replace its parent,
        else:
            parent = node #son to be parent
            print node.data, "node data"
            successor = node.right# node's right son to be the descendant
            if successor:
                print successor.data, "successor data"
            # find the the smallest son of the successor
            if successor.left is not None:
                print successor.left.data, "successor.left.data"
            while successor.left:
                print "**"
                parent = successor
                successor = successor.left
            #find the leftest son
            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right
            
    def print_tree(self):
        if self.left:
            self.left.print_tree()
            
        print self.data
        if self.right:
            self.right.print_tree()
            
        
    def print_tree1(self):
        print self.data
        if self.left:
            self.left.print_tree1()
        if self.right:
            self.right.print_tree()
            
    def print_tree2(self):
        if self.left:
            self.left.print_tree2()
        if self.right:
            self.right.print_tree2()
        print self.data


def main():
    a = [3,10,1,6,4,7,14,13]
    root = Node(8)
    for i in a:
        root.Insert(i)
    print "print data in pre_Order\n"
    root.print_tree()

    print"print tree in in_order\n"
    root.print_tree1()

    print "print tree in post order:"
    root.print_tree2()

    root.delete(1)
    print "1 was deleted"
    root.delete(3)
    root.delete(14)
    print "after deletion\n"
    
    print "print data in pre_Order\n"
    root.print_tree()

    print"print tree in in_order\n"
    root.print_tree1()

    print "print tree in post order:"
    root.print_tree2()

if __name__=="__main__":
    main()


















    
