# We use @property decorator on any method in the class to use the method as a property

class student:
    def __init__(self, math_marks, phy_marks, english_marks):
        self.math = math_marks
        self.phy = phy_marks
        self.english = english_marks

    @property
    def percentage(self):
        return str((self.math + self.phy + self.english)/3) + " %"

stu = student(100,90,80)
print(stu.percentage)

stu.phy = 100
print(stu.percentage)