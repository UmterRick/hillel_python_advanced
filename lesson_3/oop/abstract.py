from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def move(self):
        raise NotImplementedError


class Boat(Vehicle):
    def move(self):
        print("Swim")

class Car(Vehicle):
    ...

# v = Vehicle() Cant create instance of abstract class -> Error
b = Boat()
print(b.move())

c = Car()
# c.move()