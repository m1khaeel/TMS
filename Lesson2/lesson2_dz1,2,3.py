
# ПРИМЕР 1
# a = (3, 2)
# b = (3, 2)
# c = (3, 2)
# print(id(a), id(b), id(c), '\n')

# ПРИМЕР 2
# d = (1, 2, 3)
# e = [1, 2, 3]
# print(id(d), id(e), '\n')

# ПРИМЕР 3
a = (3, 2)
b = (3, 2)
c = (3, 2)
d = (1, 2, 3)
e = [1, 2, 3]

a = list(a)
b = set(b)
print(id(a), id(b), id(c), '\n')
print(id(set(d)), id(set(e)), '\n')
