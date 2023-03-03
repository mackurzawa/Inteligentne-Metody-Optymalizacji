import numpy as np


def add_vertex(m, remaining, cycle):
    m2 = []
    for r in remaining:
        m3 = []
        for v in range(len(cycle)-1):
            m3.append(m[cycle[v]][r] + m[r][cycle[v+1]] - m[cycle[v]][cycle[v+1]])
        m3.append(m[cycle[0]][r] + m[r][cycle[-1]] - m[cycle[0]][cycle[-1]])
        m2.append(m3)

    regrets = []
    for v in m2:
        if len(v) > 1:
            temp_v = sorted(v)
            regrets.append(temp_v[1] - temp_v[0])
        else:
            regrets.append(-v[0])

    vertex_add_index = np.argmax(regrets)
    where_add = np.argmin(m2[vertex_add_index]) + 1
    vertex_add = remaining[vertex_add_index]

    cycle.insert(where_add, vertex_add)
    remaining.remove(vertex_add)

    return cycle, remaining


def greedy_regret(m, starting_vertex):
    vertex_1 = starting_vertex
    vertex_2 = np.argmax(m[vertex_1])

    cycle_1 = [vertex_1]
    cycle_2 = [vertex_2]

    remaining = list(range(len(m)))
    remaining.remove(vertex_1)
    remaining.remove(vertex_2)

    for i in range(len(m)//2 - 1):
        cycle_1, remaining = add_vertex(m, remaining, cycle_1)
        cycle_2, remaining = add_vertex(m, remaining, cycle_2)

    return cycle_1, cycle_2