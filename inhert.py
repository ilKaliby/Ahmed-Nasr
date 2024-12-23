class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def make_sound(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says Tweet!"

    def fly(self):
        return f"{self.name} is flying."


dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Chirpy")

print(dog.eat())
print(dog.make_sound()) 
print(cat.eat())
print(cat.make_sound())

print(bird.eat()) 
print(bird.make_sound())  
print(bird.fly()) 
