from datetime import datetime, timedelta

def time_f(n, list):
    for i in range(1, n):
        list.append(str(t - timedelta(seconds=-i)))

t = datetime.now()
lst = []
n = int(input("Введите n: "))

time_f(n, lst)
print(lst, '\n', t)






