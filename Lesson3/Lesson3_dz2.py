

while True:
    a = input("Как вас зовут? ")
    try:
        b = int(input("Сколько вам лет? "))
        if b <= 0:
            b = int(input("Ошибка, повторите ввод: "))
        elif b < 10:
            print("Привет, шкет ", a)
        elif b in range(10, 18):
            print("Как жизнь? ", a)
        elif b in range(18, 100):
            print("Что желаете? ", a)
        else:
            print(a, "Вы лжете - в наше время столько не живут")
    except (ValueError, Exception):

        b = int(input("Ошибка, повторите ввод: "))
        if b <= 0:
            b = int(input("Ошибка, повторите ввод: "))
        elif b < 10:
            print("Привет, шкет ", a)
        elif b in range(10, 18):
            print("Как жизнь? ", a)
        elif b in range(18, 100):
            print("Что желаете? ", a)
        else:
            print(a, "Вы лжете - в наше время столько не живут")
