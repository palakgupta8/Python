class student:
    def __init__(self, name, math_marks, scince_marks, physics_marks):
        self.name = name
        self.math_marks = math_marks
        self.scince_marks = scince_marks
        self.physics_marks = physics_marks
        print(self.name, self.math_marks, self.scince_marks,self.physics_marks)
        
    @staticmethod
    def s():
        print("static method")
    
    def average(self):
        return (self.math_marks+self.scince_marks+self.physics_marks)/3
    
s1 = student("palak", 100,100,100)
s1.s()
print(s1.average())