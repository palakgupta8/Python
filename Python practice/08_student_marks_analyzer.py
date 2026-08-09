value1= int(input("enter frst student marks: "))
value2= int(input("enter sec student marks: "))
value3= int(input("enter third student marks: "))
value4= int(input("enter fourth student marks: "))
value5= int(input("enter fifth student marks: "))

Student = {"palak":value1, "ridhi":value2, "kajal":value3,"shivani":value4,"ammu":value5}

highest_marks = max(Student.values())

for name,mark in Student.items():
    if mark == highest_marks:
        print("topper", name)
        print("highest", mark)
        print("Average", sum(Student.values())/len(Student.values()))
    if mark <=50:
        print(name,"fail")
    else:
        print(name,"pass")