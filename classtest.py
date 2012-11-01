class Student:

    def __init__(self, name="John Doe", course=[],email = "example@gmail.com", photo_number="716445445"
                 ,degree = "MS"):
        self.name = name
        self.course = course
        self.email = email
        self.photo_number = photo_number
        self.degree = degree
        print"create a class instance for "+ name


    def printDetail(self):
        print "name", self.name
        print "course", self.course
        print "email", self.email
        print "photo_number", self.photo_number
        print "degree", self.degree

    def enroll(self, course):
        self.course.append(course)




student1 = Student("Mary",["L456"])

print "Input the cource which", student1.name, "is enrolled in.\n"

newcourse = raw_input("Type the course number or 'stop'\n")


while newcourse !="stop":
    student1.enroll(newcourse)
    
    print "Input the course which", student1.name, "is enrolled in.\n"
    
    newcourse = raw_input("Type the course number or 'stop'")

student1.printDetail()
                      
