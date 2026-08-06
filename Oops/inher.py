class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
           print("name", self.name)
           print("salary", self.salary)
           print("department", self.department)

class Developer(Employee):
     pass

dev = Developer("palak", 50000, "IT")
dev.display()
     
