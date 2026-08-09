name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

with open("student.txt", "a") as file:
    file.write("--------------------\n")
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")
    file.write("--------------------\n")

print("Student details saved successfully.")