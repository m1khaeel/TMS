

def rec_search(s_dict: dict, val: str, deep: int, parent: None):
    for k, v in s_dict.items():
        if isinstance(v, dict):
            rec_search(v, val, deep + 1, parent = k)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    rec_search(i, val, deep + 1, parent = k)
                else:
                    if i == val:
                        parent = k
                        print(f"{val} is found on a deep {deep}, parent = {parent}")
                        continue

        else:
            if v == val:
                parent = k
                print(f"{val} is found on a deep {deep}, parent = {parent}")
                continue


deep = 0
s_dict = {
    "key1": {
        "key2": {
            "key3": [
                "John",
                {
                    "key4": "Bob",
                    "key5": "Alex",
                    "key6": {
                        "key7": [
                            {
                                "key7": "Jessica",
                                "key8": {
                                    "key9": [
                                        "Alex"
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
    "key4": "Kate"
}

rec_search(s_dict, "Kate", 0, None)
print(len(s_dict))








