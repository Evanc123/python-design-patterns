from abc import ABC, abstractmethod


# Abstract Products
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Plant(ABC):
    @abstractmethod
    def grow(self):
        pass


# Concrete Products
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Tree(Plant):
    def grow(self):
        return "Growing tall."


class Flower(Plant):
    def grow(self):
        return "Blooming."


# Abstract Factory
class EcosystemFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def create_plant(self):
        pass


# Concrete Factory
class ForestEcosystemFactory(EcosystemFactory):
    def create_animal(self):
        return Dog()

    def create_plant(self):
        return Tree()


class UrbanEcosystemFactory(EcosystemFactory):
    def create_animal(self):
        return Cat()

    def create_plant(self):
        return Flower()


# Client Code
def ecosystem_description(factory: EcosystemFactory):
    animal = factory.create_animal()
    plant = factory.create_plant()
    print(animal.make_sound())
    print(plant.grow())


forest_factory = ForestEcosystemFactory()
ecosystem_description(forest_factory)

urban_factory = UrbanEcosystemFactory()
ecosystem_description(urban_factory)
