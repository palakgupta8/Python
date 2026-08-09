Number = [1,2,2,3,4,4,7,8,9,10] 
unique = [] 
for num in Number: 
    if num not in unique: 
        unique.append(num) 
print(unique)