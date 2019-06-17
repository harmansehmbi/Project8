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

    # Over writing --> Constructor will be created and old will be removed
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# s1 = Student()      # Student.__init__(s1, )
##s1 = Student("John", "+91 98076 09876", "john@gmail.com", "pass345", True, "ABC", 98776) # Gives an error
##print("s1 is: ", s1)

s2 = Student("Fionna", "+91 98333 21111")
print(("s2 is: ", s2))

