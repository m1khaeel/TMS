

my_list = list(range(1, 51))
res = []
for x in my_list:
    res.append(my_list[len(my_list) - x])
print(res, '\n')

