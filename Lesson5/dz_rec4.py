

def rec_search(s_dict: dict, new_dict: dict, val: str, deep: int, parent: None):
    for k, v in s_dict.items():
        if isinstance(v, dict):
            rec_search(v, new_dict, val, deep + 1, parent = k)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    rec_search(i, new_dict, val, deep + 1, parent = k)
                else:
                    if i == val:
                        parent = k
                        new_dict = {'val': val, 'parent': parent, 'deep': deep}
                        print(new_dict)
        else:
            if v == val:
                parent = k
                new_dict = {'val': val, 'parent': parent, 'deep': deep}
                print(new_dict)

new_dict = {}
deep = 0
s_dict = {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Alex',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark']  # deep 6
                                    }
                                ]
                            }
                        }
                    ]
                },
            },
            'key8': 'Robert'  # deep 1
        }
    }

rec_search(s_dict, new_dict, "Mark", 0, None)









