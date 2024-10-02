## creating class
class Student:

    ## creating the Constructotor
    # default constructor
    def __init__(self):
        pass
        
    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in Database..")

    # Creating methods
    def welcome(self):
        print("welcome Students",self.name)


## creating object (instance)
s1 = Student("Ajit",97)

print(s1.name, s1.marks)
print(s1.welcome())


s2 = Student("Parshuram",80)
print(s2.name, s2.marks)


