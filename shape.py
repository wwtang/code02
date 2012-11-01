"""example of class inheritance"""
class Shape:
    """The base class"""
    def __init__(self, side=1):
        self.side = side

class Cirlce(Shape):
    """Circle class inherited from shape"""
    def __init__(self, side=1, x, y):
        self.side = side
        self.x = x
        self.y = y
        
class Square(Shape):
    """Square class inherited from Shape"""
    def __init__(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y
