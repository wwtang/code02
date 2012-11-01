""" circle modeuls : contains the Circle class"""
class Circle:
    """Circle class
    all_circles servers as a recorder here
    """
    pi = 3.1415926
    all_circles = []
    
    def __init__(self, radius=1):
        """ Create a circle with a given radius"""
        self.radius = radius
        self.__class__.all_circles.append(self)
        #self.radius = 10

    def area(self):
        """Caculate and return the area of the cirlce"""
        #return self.radius*self.radius*Circle.pi
        return self.__class__.pi*self.radius*self.radius

    @staticmethod
    def total_area():
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total
