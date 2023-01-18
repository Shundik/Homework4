dict_1 = {
    'key1': 'dog',
    'key2': 'cat',
}
new_dict1 = {y: x for x, y in dict_1.items()}
print(new_dict1)
