def simple_decorator(decorator):
	def new_decorator(f):
		g = decorator(f)
		g.__name__ = 

	new_decorator.__name__ = decorator.__name__
	new_decorator.__doc__ = decorator.__doc__
	new_decorator.__dict__.update(decorator.__dict__)
	return new_decorator