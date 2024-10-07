class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg marks is:", sum//3)


    @staticmethod
    def hello():
        print("hello")

s1 = Student("Rakesh", [97,80,70])
s1.get_avg()

s1.name = "captain"
s1.get_avg()

s1.hello()
