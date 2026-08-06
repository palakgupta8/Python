class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("name", self.name)
        print("age", self.age)
        print("course", self.course)

student1 = Student("Alka", 30, "HR")
student1.display()
print("................")

student2 = Student("Anu", 40, "Manager")
student2.display()
print("................")

student3 = Student("Garmine", 25, "QA")
student3.display()
