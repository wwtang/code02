class Foo:
    def __init__(self, printme):
        print printme

    
class Foo2:
    def setx(self, x):
        print x

        
class Bar:
    def __init__(self, iamthis):
        self.iamthis = iamthis

    def __str__(self):
        return self.iamthis

    def __repr__(self):
        return "Bar (%s)" % self.iamthis





