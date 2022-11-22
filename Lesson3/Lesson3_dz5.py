from random import randint

x = int(input("Введите число: "))
n = randint(1, 10)
while x != n:
    x = int(input(" Введите число заново: "))
else:
    print("Вы угадали число: ", x)