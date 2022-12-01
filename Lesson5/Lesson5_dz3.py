from datetime import datetime, timedelta

def time_f(n, my_list):
    for i in range(n):
        my_list.append(str(t - timedelta(seconds=i)))
    my_list.reverse()

t = datetime.now()
lst = []
n = int(input("Введите n: "))

time_f(n, lst)
print(lst, '\n', t)






