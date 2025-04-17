# with open("decorators.py", "r") as file:
#
#     for i in file.readlines():
#         print(i)


# file = open("decorators.py", "r")
# for i in file.readlines():
#     print(i)
    # x = 10 / 0
# file.close()


class MyContextManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()
        print(exc_type, exc_value, exc_tb)



with MyContextManager("decorators.py") as f:
    print(f.closed)
    x = 10/0

print(f.closed)
