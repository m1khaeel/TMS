

some_couple = ('воин', 'шалаш', '22', 'поле', 'казак', 'lol', 'batya')

res = filter(lambda x: x[::] == x[::-1], some_couple)
print(list(res))


