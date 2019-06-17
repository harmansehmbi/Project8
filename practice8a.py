class Student:
    pass

s1 = Student()
s2 = Student()

s1.name = "John"
s1.phone = "+91 98732 13333"
s1.email = "john@example.com"
s1.password = "redff"
s1.isCollegeTraining = True
s1.collegename = "GNE"
s1.roll = 45

s2.name = "Fionna"
s2.phone = "+91 99999 11243"
s2.email = "fionna@example.com"
s2.password = "ijkff"
s2.isCollegeTraining = True
s2.collegename = "ABC"
s2.roll = 78

print(s1.__dict__)
print(s2.__dict__)


# Challenge : No standardization
# Solution : Constructors