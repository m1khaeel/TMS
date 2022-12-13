

per1 = input("1 stroka: ")
per2 = input("2 stroka: ")
per3 = input("3 stroka: ")
per4 = input("4 stroka: ")


f = open('example_file.txt', 'w')
try:
    f.write(f'{per1}\n')
    f.write(f'{per2}\n')

finally:
    f.close()

f = open('example_file.txt', 'a')
try:
    f.write(f'{per3}\n')
    f.write(f'{per4}\n')
finally:
    f.close()
f = open('example_file.txt')
k = f.read()
print(k)
