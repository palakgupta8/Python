def numbers(n):
    for i in range(1, n + 1):
        yield i


for number in numbers(5):
    print(number)