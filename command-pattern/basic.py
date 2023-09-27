from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# ConcreteCommand Class
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver Class
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


# Invoker Class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Client Code
if __name__ == "__main__":
    # Receiver
    light = Light()

    # Concrete Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Invoker
    remote = RemoteControl()

    # Execute Commands
    remote.set_command(light_on)
    remote.press_button()

    remote.set_command(light_off)
    remote.press_button()
