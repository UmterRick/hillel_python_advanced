class Car:
    def __init__(self, wheels, hp, color):
        ...
    def start(self):
        print(f"{self.__class__.__name__} stars")

    def stop(self):
        ...
        print(f"{self.__class__.__name__} stops")

class Truck(Car):
    ...

class Plane:
    def fly(self):
        print("I can fly")

    def start(self):
        print("Going to the sky")


class FlyingTruck(Plane, Truck): # MRO (diamond problem)
    ...


car = Car(4, 120, "blue")
car.start()
car.stop()

t = Truck(6, 600, "black")
t.start()
t.stop()


ft = FlyingTruck(6, 1200, "white")
ft.start()
ft.fly()

