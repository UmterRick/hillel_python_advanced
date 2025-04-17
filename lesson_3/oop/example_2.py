class A:
    def method(self):
        print("A")



class B(A):
    def method(self):
        print("B")


class Animal:
    def voice(self) -> None:
        print("rrrrrr")



class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("Wuff")


b = B()
b.method()