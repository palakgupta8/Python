Name = input("Enter student name: ")

Math = int(input("enter math marks: "))
Science = int(input("enter science marks: "))
English = int(input("enter english marks: "))
Hindi = int(input("enter hindi marks: "))
Computer = int(input("enter computer marks: "))

total = Math+Science+English+Hindi+Computer
percentage = total/500*100

print("Total", total )
print("Percent", percentage)

if percentage >= 90:
    print("Grade A")

elif percentage >= 75:
    print("Grade B")

elif percentage >= 60:
    print("Grade C")

elif percentage >= 40:
    print("Grade D")

else:
    print("Grade F")

if percentage>=40:
    print(Name,"is pass")
else:
    print(Name,"is fail")