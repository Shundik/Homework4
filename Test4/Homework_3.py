dict_1 = {
    "house": 1,
    "water": 1,
    "apple": 2,
    "milk": 3,
}
print(dict_1)
d = {}


def meaning():
    for i in dict_1.values():
        if not i in d:
            d[i] = 1
        else:
            d[i] += 1


meaning()
print(d)
