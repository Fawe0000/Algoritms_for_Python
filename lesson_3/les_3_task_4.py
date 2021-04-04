#4. Определить, какое число в массиве встречается чаще всего.

import random

mass = [random.randint(-10, 10) for _ in range(int(input('Сколько элементов должно быть в генерируемом массиве?')))]
print(f'Массив: {mass}')

num = 0
max_num = 1
for i,n in enumerate(mass):
    spam = 1
    for k in range(i + 1, len(mass)):
        if n == mass[k]:
            spam += 1
    if spam > max_num:
        max_num = spam
        num = n

if max_num > 1:
    print(f'Число {num}, встречается {max_num} раз(а)')
else:
    print('Все элементы массива встречаются по 1 разу')