"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

import random
from collections import deque


def generate_graph(num):
    graph = [list({random.randint(0, n) for j in range(random.randint(1, n)) if j != i}) for i in range(n)]
#    graph = [
#        [1, 3, 4],  # 0
#        [2, 5],     # 1
#        [1, 6],     # 2
#        [1, 5, 7],  # 3
#        [2, 6],     # 4
#        [6],        # 5
#        [5],        # 6
#        [6],        # 7
#    ]
    return graph


def deep_walk(graph, start, finish, g_path, cost, best_cost):

    g_path.append(start)
    cost += 1
    for i, vertex in enumerate(graph[start]):
        if vertex == finish:
            g_path.append(vertex)
            path_i[cost] = deque(g_path)
            path_i[cost] = list(path_i[cost])
            cost = 0

        elif not is_visited[start][i]:
            start = vertex
            is_visited[start][i] = True
            deep_walk(graph, start, finish, g_path, cost, best_cost)

        return
    return path_i


n = int(input('Введите количество вершин в графе: \n'))
g = generate_graph(n)
print(*g, sep='\n')
is_visited = [[False for _ in range(len(g[j]))] for j in range(len(g))]

g_path = []
path_i = {n+1: 'нет решения'}
best_cost = 0
cost = 0
cost_i = 0
s = int(input("Введите вершину начала: "))
f = int(input("Введите вершину конца: "))

deep_walk(g, s, f, g_path, cost, best_cost)
print('*'*50)
print(f'Варианты пути из вершины "{s}" в вершину "{f}":')
k = 0
for i, path in enumerate(path_i):
    if i == 0 :
        k = 1
    else:
        print(f' Вариант пути №{k}, длина пути = {path}: {path_i[path]}')
        k = 0
if k == 1:
    print(path_i[n+1])
