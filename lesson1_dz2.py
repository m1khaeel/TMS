# ПРИМЕР С МОДУЛЯМИ
# x = int(input("Введите х: "))
# y = int(input("Введите у: "))

# a = (abs(x) - abs(y)) / (1 + abs(x * y))
# print(a)

# СРЕЗЫ:


x = "aaaaaBccBddBeeBffBggB"
a = x[5::3]
print(a)

y = "AAAABBBBCCCCDDDDFFFF"
b = y[:4]
c = y[4:8]
d = y[8:12]
e = y[12:16]
f = y[16:]
print(b + c + d + e + f)

v = "PYTHON"
n = v[::-1]
print(n)
