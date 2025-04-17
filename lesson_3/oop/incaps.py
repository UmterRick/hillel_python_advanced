class ExampleClass:
    def __init__(self):
        self.a = 10
        self._b = 10
        self.__c = 10

    def __private_method(self): # private
        print("Hi")

    def _protected_method(self): # protected
        print("Hello")

    def method(self):
        self.__private_method()
        self._protected_method()
        return "Hello World"



e = ExampleClass()

e.method()
print(e.a)
print(e._b)
e.__c # Error
e._protected_method()
# e.__private_method()
