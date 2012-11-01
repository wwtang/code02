class Foo:
    def bar(self, message):
        print message

        

class FooP:
    def bar(self, message):
        print message

class FooC(FooP):
    def bar(self, message):
        FooP.bar(self, message)

class FooCC(FooP):
    def bar(self, message):
        super(FooCC, self).bar(message)
        


        
class A:
    def __init__(self):
        print "Enter A"
        print "Leave A"

class B:
    def __init__(self):
        print "Enter B"
        A.__init__(self)
        print "Leave B"

        
class Complex:
    def __init__(self, realpart, imagepart):
        self.r = realpart
        self.i = imagepart
        self.l = "we are here"


class Bag:
    def __init__(self):
        self.data = []
        self.index = 0
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.data.append(x)
        self.data.append(x)

class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)

class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)



    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
    __update =update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_orighin(self):
        return((self.x**2) + (self.y**2)) **0.5
    def areas(self):
        return self.x *self.y





class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        print "(Initializeing %s)" % self.name

        Person.population +=1

    def __del__(self):
        print "Say bye! %s" %self.name

        Person.population -=1
        if Person.population ==0:
            print "I am the last one"
        else:
            print "There are still %d  people left" % Person.population

    def sayHi(self):
        print "Hi My name is %s"% self.name

    def howMany(self):
        if Person.population ==1:
            print "I am the only one person here."
        else:
            print "We have %d persons here"% Person.population



class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "Initializing SchoolMember ...%s"% self.name

    def tell(self):
        print "Name: %s, Age: %s"%(self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print "Initializing Teacher... %s" % self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Salary: %d" % self.salary

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name ,age)#inieritant from SchoolMember
        self.marks = marks
        print "Initialized Student %s"% self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Marks %d"%self.marks
    

    
