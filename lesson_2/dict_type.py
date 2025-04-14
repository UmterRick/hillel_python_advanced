key = "name"
value = "Vlad"
my_dict = {key: value}
key_h = hash(key)
print(key_h)

hash_table_size = 4
record_index = key_h % hash_table_size
print(record_index)
key_2 = "address"
value = "street Stree"
my_dict.update({key_2: value})
key_2_h = hash(key_2)
print(key_2_h)
record_index = key_2_h % hash_table_size
print(record_index)


"""
idx| hash | key | value |
__________________
 0 |
 1 |
 2 | 6224246400616650586 | name | Vlad
 3 |
 ....
 3333 | -8301420995861900406 | address | street Street
 
"""
