

def rec_reverse(source_list):
    for i in source_list:
        list1.append(source_list[-i])
    return

list1 = []
source = [1, 2, 3, 4, 5]
rec_reverse(source)

print(list1)
