#Basic Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Makes a Noise"

#Child Class Dog
class Dog(Animal):
    def speak(self):
        return "Guau"

#Child Class Cat
class Cat(Animal):
    def speak(self):
        return "Miau"

#Using the Classes
dog = Dog("Firulais")
cat = Cat("Michi")

print(dog.speak())  # Guau
print(cat.speak())  # Miau
#