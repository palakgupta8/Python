password = input("enter password: ")

digit=False
lower=False
upper=False

if len(password) >= 8:
    for check in password:
        if check.isdigit():
            digit=True

        if check.islower():
            lower=True

        if check.isupper():
            upper=True

    if digit==True and lower==True and upper==True:
        print("valid password")
    else:
        print("please enter valid password")
else:
    print("Password must contain at least 8 characters.")