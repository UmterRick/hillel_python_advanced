"""
small_int
int
big_int
"""

x = 10 ** 99 * 2.17
# print(x)


import ctypes
import sys


def inspect_int(n):
    address = id(n)
    size = sys.getsizeof(n)
    raw = (ctypes.c_ubyte * size).from_address(address)
    print(f"int: {n}, address: {hex(address)}, size: {size}")
    print("Raw memory:", list(raw))


inspect_int(x)

print(float('inf'))
print(float('-inf'))
infinity = float('inf')
print(sys.getsizeof(infinity))
print(sys.getsizeof(21))