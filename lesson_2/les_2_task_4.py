#4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def generator_r(n):
    ryad_i = -2
    sum_r = 0
    s = ''
    for i in range(n):
        ryad_i /= -2
        sum_r = sum_r + ryad_i
        s = s + str(ryad_i) + ', '
    return s, sum_r

gs, gsum_r = generator_r(int(input("Введите количество элементов (n) для ряда '1, -0.5, 0.25, -0.125,…': ")))
print(f'Для конечного ряда:\n'
      f'{gs}\n'
      f'сумма всех элементов = {gsum_r:.4f}')