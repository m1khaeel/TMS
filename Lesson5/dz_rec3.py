

def rec_f(source_list):
    for x in source_list:
        if isinstance(x, list):
            rec_f(x)
        else:
            res.append(x)

res = []
list1 = [[1, 2], 1, [[3, 4, [5, 6]]], [7, 8, [9, 10, [11, [12]]]]]
rec_f(list1)
print(res, '\n', len(list1))