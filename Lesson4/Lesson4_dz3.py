

my_list = list(range(1, 101))

res1 = [x for x in my_list if x % 10 == 0]
result = [x * 10 if x % 4 != 0 else x * 2 for x in res1]

print(result, '\n')