"""
int array[5] = [1, 3, 5, 7, 9]
array[2] # 5
array[999999]
n = 999999
address_of_value_of_index_n = address_of_first_element_of_array + (size_of_array_elements * index_i)
array[get_by_index_i] -> O(1)

a = True
b = 1
c = "Hello"
d = (1, 3, 4)
my_python_list = [a, b, c, d]
# my_python_list = [addr_of_a, addr_of_b, addr_of_c, addr_of_d]

Was here:
_______________________________________________
| a | b | c | d | bdcas | 12321 | 9089  | True

Now Here:
_______________________________________________
| a | b | c | d | e |   |   |   | bdcas | 12321 | 9089  | True
my_list.append(e)

List append:
Avg = O(1)
Best = O(1)
Worst = O(n)

"""
#
# list_a = ["1", "2", "3", "4"]
# print(f"addr_index_0 = {id(list_a[0])}")
# print(sys.getsizeof(list_a))
# list_b = []
# for i in range(1000):
#     list_b.append(i)
#
# for i in range(4, 5000):
#     list_a.append(f"{i}" * 100)
#     print(f"addr_index_0 = {id(list_a[0])}")
#     print()


def func():
    a = 2
    b = 3
    return a, b


result = func()
res_1, res_2, res_3 = func()
print(result, type(result))
print(res_1, res_2, type(result))