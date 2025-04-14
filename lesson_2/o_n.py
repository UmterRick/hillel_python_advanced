import sys

input_list = [1, 2, 3, 4]
for i in input_list:
    for j in input_list:
        if j == 1:
            print(i)

n = len(input_list)

"""
O(1)
worst O(n)
average O(n)
best O(n)
"""

