from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class FlyingAnimal(Animal):
    @abstractmethod
    def fly(self):
        pass


class Dog(Animal):
    def eat(self):
        return "Dog eating"


class Parrot(FlyingAnimal):
    def eat(self):
        return "Parrot eating"

    def fly(self):
        return "Parrot flying"

dog = Dog()
parrot = Parrot()

print(dog.eat())
print(parrot.eat())
print(parrot.fly())
