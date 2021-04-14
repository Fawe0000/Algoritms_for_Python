import sys
import random

print(sys.version, sys.platform)


# функция подсчёта памяти, используемой для хранения переменных
# сделал на базе рассмотренного на занятии примера

def show_size(x, level=0):
    size_par = sys.getsizeof(x)
#    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


# задача 3 из урока 3:
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

kol_i = int(input('Сколько элементов должно быть в генерируемом массиве?'))
mass = [random.randint(-10, 10) for _ in range(kol_i)]

# решение 1

mn1,mx1 = 0,0

for i,n in enumerate(mass):
    if n > mx1:
        mx1, index_max = n,i
    elif n < mn1:
        mn1, index_min = n,i

mass[index_min], mass[index_max] = mass[index_max], mass[index_min]
print(f'Массив с поменянными местами минимальным ({mn1}) и максимальным ({mx1}) элементами:\n'
      f' {mass}')
print(f'Решение 1, использовано памяти: '
      f'{show_size(kol_i) + show_size(mass) + show_size(mn1) + show_size(mx1) + show_size(index_min) + show_size(index_max) + show_size(i) + show_size(n)}'
      f' байт')
print('-' * 25)
#---------------------------------------------------------------------
# решение 2

arr = [0] * kol_i
for i1 in range(kol_i):
    arr[i1] = int(random.randint(-10, 10) * 100)
    print(arr[i1], end=' ')
print()

mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('Меняем местами arr[%d]=%d и arr[%d]=%d ' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

for i in range(kol_i):
    print(arr[i], end=' ')
print(f'\n Решение 2, использовано памяти: '
      f'{show_size(kol_i) + show_size(arr) + show_size(i1) + show_size(mn) + show_size(mx) + show_size(imn) + show_size(imx) + show_size(i)}'
      f' байт')
print('-' * 25)
#---------------------------------------------------------------------
# решение 3

def getIndex(array):
    imin = array.index(min(array))
    imax = array.index(max(array))
    if imin > imax:
            return imin, imax, show_size(imin) + show_size(imax)
    return imax, imin, show_size(imin) + show_size(imax)

lst = [random.randint(-10, 10) for _ in range(kol_i)]
print(f'Массив {lst}')
lst[getIndex(lst)[0]], lst[getIndex(lst)[1]] = lst[getIndex(lst)[1]], lst[getIndex(lst)[0]]
print(f'Массив с поменянными местами минимальным и максимальным элементами:\n'
      f' {lst}')
print(f'Решение 3, использовано памяти: '
      f'{show_size(kol_i) + show_size(lst) + getIndex(lst)[2]}'
      f' байт')

#---------------------------------------------------------------------
#Python = 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19)
# платформа = [MSC v.1925 32 bit (Intel)] win32

# ИТОГ подсчёта памяти:
# Решение 1, использовано памяти: 398 байт
# Решение 2, использовано памяти: 396 байт
# Решение 3, использовано памяти: 344 байт
# Вывод: Третье решение - самое экономное в использовании памяти для переменных

