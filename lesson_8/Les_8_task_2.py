#2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    begin = start
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    edge = {}
    for i, vertex in enumerate(parent):
        if vertex > -1:
            edge[i] = deque([vertex, i])

            while vertex > -1:
                vertex = parent[vertex]
                if vertex > -1:
                    edge[i].appendleft(vertex)

            edge[i] = set(edge[i])
        elif i == begin:
            edge[i] = {0}
        else:
            edge[i] = {float('inf')}

    return edge

print('*'*25, f'\n для графа:')
print(*g, sep='\n')
s = int(input('введите вершину старта: \n'))
print(f'вершины, которые нобходимо обойти:')
print(dijkstra(g, s))
