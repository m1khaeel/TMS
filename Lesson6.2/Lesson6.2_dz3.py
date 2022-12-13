

import json

my_dict = {
     117691: ('John', 31),
    190223: ('Mike', 27),
    345634: ('Rin', 19),
    237567: ('Kolya', 11),
    569037: ('Igor', 48)
}
my_dict_json = json.dumps(my_dict)
with open("my_dict.json", "w") as my_file:
    my_file.write(my_dict_json)






