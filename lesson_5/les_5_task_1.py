# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict
from collections import deque


kol_com = int(input("Введите количество предприятий: "))
companies = OrderedDict()
minor_company = deque()
major_company = deque()
avg_company = deque()
print('-' * 25)
for i in range(kol_com):
    name = input(f"Введите наименование {i+1}-го предприятия: ")
    companies[name] = float(input(f"Введите годовую прибыль {i+1}-го предприятия: "))
    print('-'*25)

avg_com = sum(companies.values()) / len(companies)

print(f"Средняя прибыль (за год для всех {kol_com} предприятий) составляет {avg_com:.02f}")
print('-' * 25)
for name, profit in companies.items():
    if profit > avg_com:
        major_company.append(name)
    elif profit < avg_com:
        minor_company.append(name)
    else:
        avg_company.append(name)

print(f'Список предприятий, прибыль которых:')
if major_company:
    print(' - выше средней: ')
    for name in major_company:
       print(f' ---- {name}')
if minor_company:
    print(f' - ниже средней: ')
    for name in minor_company:
       print(f' ---- {name}')
if avg_company:
    print(f' - равна средней: ')
    for name in avg_company:
       print(f' ---- {name}')
