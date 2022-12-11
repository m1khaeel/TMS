

def my_func():
    n = input("Введите число: ")
    if n.isdigit():
        n = int(n)
        if n > 0:
            print(f"Вы ввели положительное целое число:  {n}")
        else:
            print(f"Вы ввели : {n}")
    try:
        n = int(n)
        if n < 0:
            print(f"Вы ввели отрицательное целое число:  {n}")
    except:
        try:
            n = float(n)
            if n > 0:
                print(f"Вы ввели положительное дробное число:  {n}")
            else:
                print(f"Вы ввели отрицательное дробное число:  {n}")
        except:
            print(f"Вы ввели некорректное число:  {n}")

my_func()