class Student:
    # self is reference variable which will hold hashcode of current object
    # __init__ is known as constructor
    # Constructor is property of class

    def __init__(self, name, phoneNumber, email, password, isCollegeTraining, collegeName, rollNum):
        print(">> self is: ", self)
        self.fullName = name
        self.phone = phoneNumber
        self.email = email
        self.password = password
        self.isCollegeTraining = isCollegeTraining
        self.collegeName = collegeName
        self.rollNum = rollNum


    def showStudentDetails(self):
        print("Details of", self.fullName)



# s1 = Student()      # Student.__init__(s1, )
s1 = Student("John", "+91 98076 09876", "john@gmail.com", "pass345", True, "ABC", 98776)
print("s1 is: ", s1)

s2 = Student("Fionna", "+91 98333 21111", "fionna@gmail.com", "pass987", True, "ZZZ", 233096)
print(("s2 is: ", s2))

s1.age = 22
s1.vehcileNum = "PB10SW9087"

s1.fullName = "John Watson"
s2.fullName = "Fionna Fyln"

s1.showStudentDetails()
s2.showStudentDetails()