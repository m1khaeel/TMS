import json
import csv
calls = ['id', 'name', 'age', 'phone']
numbers = [375337778899, 80291111111, 6473290033, 74320316111, 3127642199]
f = open('my_dict.json')
a = f.read()
b = json.loads(a)

with open("my_dict.csv", "w") as my_file:
    wr = csv.DictWriter(my_file, fieldnames=calls)
    wr.writeheader()
    for k, v in b.items():
        for i in numbers:
            wr.writerow({'id': k, 'name': v[0], 'age': v[1], 'phone': i})




