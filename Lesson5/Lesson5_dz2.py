

def my_f(list, dict):
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

list = [1, 2, 1, 2, 4, 5, 3, 2, 1, 2, 3, 4, 4, 5, 6, 0, 2, 0, 1, 24]
dict1 = {}
my_f(list, dict1)
print(dict1)










