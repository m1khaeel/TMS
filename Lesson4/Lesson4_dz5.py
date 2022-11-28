

dict_1 = {"key1": 1,  "key2": 2,  "key3": 3,  "key4": 4,  "key5": 5}

dict_new = {dict_1[x]: x for x in dict_1}
print(dict_new)