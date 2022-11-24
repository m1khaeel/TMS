

a = input("Как вас зовут? ")
b = input("Сколько вам лет? ")
while True:
    try:
        b = int(b)
        if b <= 0:
            b = int(input("Ошибка, повторите ввод: "))
        elif b < 10:
            print(f"Привет, шкет {a}")
            break

        elif 10 <= b <= 18:
            print(f"Как жизнь? {a}")
            break

        elif 18 < b < 100:
            print(f"Что желаете? {a} ")
            break

        else:
            print(a, "Вы лжете - в наше время столько не живут")
            break

    except ValueError:
        b = input("Ошибка, повторите ввод: ")

