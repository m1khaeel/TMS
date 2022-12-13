

b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode()
b1 = s.encode('Latin1')
s1 = b1.decode('Latin1')
print(s, '\n', b1, '\n', s1)