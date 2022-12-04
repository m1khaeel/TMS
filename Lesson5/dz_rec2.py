

def rec_max(some_list):
    assert some_list
    mx = some_list[0]
    for i in some_list:
        if i > mx:
            mx = i
    return mx
list1 = [1, 0, 5, 0 ,5, 8, 7, 4, 9, 2]
res = rec_max(list1)
print(res)
