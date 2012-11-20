"""
point class
"""
class point(object):
	"""docstring for point"""
	def __init__(self, x=0, y=0):
		self.x= x
		self.y = y

	def __str__(self):
		return "x is %d, y is %s" %(self.x, self.y)
		
		
	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		return point(x,y)