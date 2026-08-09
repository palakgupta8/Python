sentence = input("enter a sen: ") 

print(f"total character is {len(sentence)}") 

print(f"total words are {len(sentence.split())}") 

count_vowel=0 
for vowels in sentence: 
    if vowels.lower() in "aeiou": 
        count_vowel+=1 
print(f"vowels: {count_vowel}") 

count_space=0 
for space in sentence: 
    if space==" ": 
        count_space+=1 
print(f"space: {count_space}")