# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’]. Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

# заполняем таблицу соответствия 16-ричных символов десятичным числам
hexatable = '0123456789ABCDEF'
table_hex = defaultdict(int)
for i,key in enumerate(hexatable):
    table_hex[key] = i

# Переводим 16-ричное число в десятичное
def hex_to_dex(string):
    dex_x = 0
    hex_string = deque(string)
    hex_string.reverse()
    for i in range(len(hex_string)):
        dex_x += table_hex[hex_string[i]] * 16 ** i
    return dex_x

# переводим десятичное число в строку 16-ричных цифр
def dex_to_hex_s(dex_x):
    hex_s_x = deque()
    while dex_x > 0:
        d = dex_x % 16
        for i in table_hex:
            if table_hex[i] == d:
                hex_s_x.append(i)
        dex_x //= 16
    hex_s_x.reverse()
    return list(hex_s_x)

hex_s_1 = input('Введите первое число в шестнадцатиричном формате: ').upper()
dex1 = hex_to_dex(hex_s_1)
hex_s_2 = input('Введите второе число в шестнадцатиричном формате: ').upper()
dex2 = hex_to_dex(hex_s_2)

print('-' * 25)
print(f'Сумма 16-ричных чисел: {list(hex_s_1)} + {list(hex_s_2)} = {dex_to_hex_s(dex1 + dex2)}')
print(f'Произведение 16-ричнеых чисел: {list(hex_s_1)} * {list(hex_s_2)} = {dex_to_hex_s(dex1 * dex2)}')