# for i in [1, 2, 3, 4, 5]:
#     print(i)


for i in "hello world":
    print(i)

# Iterable
# dunder (double underscored)/magic methods
"""
__iter__
__next__
"""

x = [1, 2, 3].__iter__()
print(x)
x = "hello".__iter__()
print(x)
x = (1, 2, 3).__iter__()
print(x)
x = {1, 2, 3}.__iter__()
x = dict().items().__iter__()
print(x)

some_dict = {"a": 1, "b": 2, "c":3}

# for i in some_dict.items():
#     print(i)

some_list = [9, 8, 7, 6, 5, 4]
some_list_iterator = some_list.__iter__()
print(next(some_list_iterator))
print(next(some_list_iterator))
print(next(some_list_iterator))
print(next(some_list_iterator))
print(next(some_list_iterator))
print(next(some_list_iterator))
# After last element
# print(next(some_list_iterator)) cause StopIteration Error

# print("Iterate through collection using while loop")
# iterator = some_list.__iter__()
# while True:
#     try:
#         el = next(iterator)
#         print(el)
#         some_list[8]
#     except StopIteration:
#         break


class MyIterator:
    def __init__(self, values):
        self.storage = values
        self.current_index = 0


    def __iter__(self):
        self.current_index = len(self.storage) - 1
        return self

    def __next__(self):
        if self.current_index < 0:
            raise StopIteration
        if self.current_index % 2 == 0:
            self.current_index -= 1
            return
        el = self.storage[self.current_index]
        self.current_index -= 1
        return el

print("Our iterable class")
a = MyIterator([1, 2, 3, 4, 5, 6])
for i in a:
    print(i)









