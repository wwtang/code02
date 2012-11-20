"""
kangaroo class
"""

class kangaroo2(object):
	def __init__(self, pouch_content=[]):
		self.pouch_content = pouch_content

	def __str__(self):
		# length = len(self.pouch_content)
		# if length > 0:
		# 	for i in range(length):
		# 		return self.pouch_content[i]
		# else:
		# 	return "No content"
		return str(self.pouch_content)

	def put_in_pouch(self,other):
		return self.pouch_content.append(other)

class Kangaroo(object):
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)
