username = "Admin"
password = 1234

attempts = 1

while attempts <= 3:

    user=input("please enter username: ")
    pas =int(input("please enter password: "))

    if user==username and pas == password:
        print("logged in successfully!!")
        break

    else:
        print("invalid username or password")
        attempts += 1

if attempts > 3:
   print("locked")