""" Inheritance with class and instance variable"""
class P:
    """ base class"""
    #class variable
    z = "hello"
    def set_p(self):
        self.x = "class P"
    def print_p(self):
        print(self.x)

class C(P):
    def set_c(self):
        self.x = "class C"
    def print_c(self):
        print(self.x)



class Mine:
    """ another class to demostrate private variable and methods"""
    def __int__(self):
        self.x = 2
        #private variable symboled by the leading double underscore
        self.__y =3

    def print_y(self):
        print self.__y
