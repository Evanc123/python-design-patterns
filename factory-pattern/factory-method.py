from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


def animal_sound(factory: AnimalFactory):
    animal = factory.create_animal()
    print(animal.make_sound())


# Client Code
dog_factory = DogFactory()
animal_sound(dog_factory)

cat_factory = CatFactory()
animal_sound(cat_factory)
