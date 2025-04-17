from os import pread

x = range(1, 10)


for i in range(10, 20, 2):
    print(i)


for i in [10, 12, 14, 16, 18]: # len(x) = 5
    print(i)


def some_generator():
    while True:
        print("Some action before yield")
        yield
        print("Some action After yield")


def range_generator(start, end, step):
    current_value = start
    while current_value < end:
        yield current_value
        current_value += step

# x = some_generator()
# print(x)
# next(x)
# print()
# next(x)
print("My own range generator")
for i in range_generator(20, 10, -2):
    print(i)


l = [i ** 2 for i in range(10)]
a = {i ** 2 for i in range(10)}
print(type(a))
b = {i ** 2: i for i in range(10)}
print(type(b))
c = (i ** 2 for i in range(10))
print(type(c))
for i in c:
    print(i)


def complex_generator(limit):
    counter = 0
    while counter <= limit:
        print("Some action before 1 yield")
        yield "Hello"
        print("Some action After 1 yield")
        print("Some action before 2 yield")
        yield "World"
        print("Some action After 2 yield")
        counter += 1


# Minimalistic pytest fixture example
def test_file():
    create_file()
    yield
    delete_file()


def my_test(test_file):
    print("Testing file")
# for i in complex_generator(20):
#     print(f">>> {i}")







