class FooP:
    def bar(self, message):
        print (message)

class FooC(FooP):
    def bar(self, message):
        FooP.bar(self, message)

class FooCC(FooP):
    def bar(self, message):
        super(FooCC, self).bar(message)
        
