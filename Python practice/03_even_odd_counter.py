numbers = [1,2,3,4,5,6,7,8,9,10]

even_count = 0
odd_count = 0

print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)
        even_count += 1

print()

print("Odd Numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num)
        odd_count += 1

print()
print(f"Total Even Numbers = {even_count}")
print(f"Total Odd Numbers = {odd_count}")