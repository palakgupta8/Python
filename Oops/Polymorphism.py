class Dog:
    def sound(self):
        print("Dog is barking")

class Cat:
    def sound(self):
        print("cat is meowing")

class Cow:
    def sound(self):
        print("cow is mooing")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()



