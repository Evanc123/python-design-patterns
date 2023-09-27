# based on https://www.youtube.com/watch?v=_BpmfnqjgzQ


import time
import random

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject: "Subject"):
        pass


class Subject(ABC):
    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def add_observer(self, observer: Observer):
        pass


class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def get_temperature(self):
        return self._temperature

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()

    def randomly_change_temperature(self):
        print("Starting to randomly change the temperature")

        while True:
            delay = random.randint(1, 3)
            print(f"Delay: {delay} seconds")
            time.sleep(delay)
            new_temp = random.randint(0, 100)
            print(f"New Temp is {new_temp}")
            self.set_temperature(new_temp)


class WeatherObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, subject: WeatherStation):
        print(
            f"Observed the weather changed at {self.name}: The temperature changed to {subject.get_temperature()}"
        )


arctic_station = WeatherStation()

first_observer = WeatherObserver("First Observer")
second_observer = WeatherObserver("Second Observer")


arctic_station.add_observer(first_observer)
arctic_station.add_observer(second_observer)

arctic_station.randomly_change_temperature()
