# 1. Определение количества различных подстрок с использованием хеш-функции.
#  Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

import hashlib

def sub_str(string: str):
    substring_summ = set()

    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            substring_summ.add(hash_str)
    return (len(substring_summ) -1)


print(f'Определение количества различных подстрок с использованием хеш-функции')
string = ''
while string == '':
    string = input(f'Введите строку\n')
    if len(string) <= 0:
         print(f'Ошибка: Строка не может быть пустой!\n {"*"*50}\nповторите ввод')

print(f'Всего в строке:\n"{string}"\n {sub_str(string)} различных подстрок')