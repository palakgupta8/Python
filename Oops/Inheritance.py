class Employee:
    def __init__(self, role, salary, dept):
        self.role = role
        self.salary = salary
        self.dept = dept

    def showDetails(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("role = ",self.role)
        print("salary = ",self.salary)
        print("dept = ",self.dept)



class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")


E2 = Engineer("palak", 23)
E2.showDetails()