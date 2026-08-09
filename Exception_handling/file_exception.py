try:
    with open("palak.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("file not exist")
