#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
kol_i = int(input('Сколько элементов должно быть в генерируемом массиве?'))
mass = [random.randint(-10, 10) for _ in range(kol_i)]
print(f'Массив: {mass}')

min,max = 0,0

for i,n in enumerate(mass):
    if n > max:
        max, index_max = n,i
    elif n < min:
        min, index_min = n,i

mass[index_min], mass[index_max] = mass[index_max], mass[index_min]
print(f'Массив с поменянными местами минимальным ({min}) и максимальным ({max}) элементами:\n'
      f' {mass}')
