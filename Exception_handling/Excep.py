 
try:
    num = int(input("enter a number : "))
    devision = 20/num
    print(devision)

except ValueError:
    print('enter a valid number')

except ZeroDivisionError:
    print("number should be zero")

else:
    print("number devisible successfully")

finally:
    print("program finished")
