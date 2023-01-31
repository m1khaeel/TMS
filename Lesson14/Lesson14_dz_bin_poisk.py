

from random import randint

my_list = []

for i in range(10):
    my_list.append(randint(1, 20))

my_list.sort()
print(my_list)

x = int(input("Введите число для поиска: "))

h_idx = len(my_list) - 1
l_idx = 0
m_idx = len(my_list) // 2

while my_list[m_idx] != x and l_idx <= h_idx:
    if x > my_list[m_idx]:
        l_idx = m_idx + 1
    else:
        h_idx = m_idx - 1
    m_idx = (l_idx + h_idx) // 2


if l_idx > h_idx:
    print("Данного числа в списке нет!!!")
else:
    print(f"Число {x} имеет индекс: {m_idx}")
