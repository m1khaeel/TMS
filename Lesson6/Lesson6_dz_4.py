from datetime import datetime
some_list = [1, 2, 3, 4, 5]
time = datetime.now()
res = []
def deco(f):
    print(f"Время выполнения функции: {time}")
    return f
@deco
def my_func1(x):
    return  x * 2
print(my_func1(5))

@deco
def my_func2(lst):
    for i in lst:
        if i % 2 != 0:
            res.append(i)
    print(res)
my_func2(some_list)

