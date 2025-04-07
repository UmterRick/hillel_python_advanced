"""
length
hash
data
kind
"""

import sys

str_1 = "helloo"
str_2 = "привіт"
str_3 = "приві💡"
str_4 = "hello💡"

size_1 = sys.getsizeof(str_1)
size_2 = sys.getsizeof(str_2)
size_3 = sys.getsizeof(str_3)
size_4 = sys.getsizeof(str_4)

print(str_1, size_1)
print(str_2, size_2)
print(str_3, size_3)
print(str_4, size_4)


print(hash(str_1))
print(hash(str_2))
print(hash(str_3))
print(hash(str_4))
print()
print(hash(str_1))
print(hash(str_2))

