"""
A class that provides an iterator generator method
"""

class Node:

    def __init__(self, name="<noname>", value="<novalue>" , children=None ):
        self.name = name
        self.value = value
        self.children = children
        if children is None:
            self.children = []
        else:
            self.children = children

    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value

    def iterchildren(self):
        for child in self.children:
            yield child
    # print information on the node and walk over all children and grandchildren

    def walk(self, level=0):
        print "%s name: %s  value: %s" %(
                get_filter(level), self.get_name(), self.get_value(),)
        for child in self.iterchildren():
            child.walk(level +1)


def walk(node, level=0):
    print "%s name: %s   value:    %s" % (
        get_filter(level), node.get_name(), node.get_value())
    for child in node.iterchildren():
        walk(child, level+1)


def get_filter(level):
    return "       "*level

def test():
    a7 = Node("gilbert", '777')
    a6 = Node("fred", " 666")
    a5 = Node("ellie", "555")
    a4 = Node("daniel", "444")
    a3 = Node("chal", "333", [a4,a5])
    a2 = Node("bill","222",[a6,a7])
    a1 = Node("alice","111",[a2,a3])
    # use the walk method to walk through the entir tree
    print "uses the mehtod: \n"
    a1.walk()
    print "+"*30
    #use the outer function to walk the entire tree
    print "use the function"
    walk(a1)

test()

    
    
