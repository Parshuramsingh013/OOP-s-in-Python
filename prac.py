class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        

    # def calculatePercentage(self):
    #     self.percentage = str((self.phy+self.chem+self.maths)//3) + " %"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.maths)//3) + " %"


stu1 = Student(97,55,69)
print(stu1.percentage)

stu1.phy = 70
# stu1.calculatePercentage()
print(stu1.phy)
print(stu1.percentage)
