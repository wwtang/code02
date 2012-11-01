class decoaratorWithoutArguments(object):

	def __init__(self, f):
		"""

		"""
		print "Inside __init__()"
		self.f = f

	def __call__(self, *args):
		print "Inside __call__()"
		self.f(*args)
		print "After self.f(*args)"

#initialize the decorator class
@decoaratorWithoutArguments
def sayHello(a1,a2,a3,a4):
	print "sayHello arguments:", a1,a2,a3,a4


print "After decoration"

print "preparing to call sayHello()"

sayHello("say", "hello", "arguments", "list")

print "after first sayHello() call"

sayHello("a", "different set ", "of ", "arguments")
print "after second sayHello() call" 