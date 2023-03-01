import random as rn
import numpy as np
from draw_graph import draw_graph


def greedy_closest_neighbour(m, starting_vertex):
    numbers = 100

    m = list(np.array(m)[:numbers, :numbers])

    remaining = list(range(numbers))

    vertex_1 = starting_vertex
    vertex_2 = np.argmax(m[vertex_1])

    remaining.remove(vertex_1)
    remaining.remove(vertex_2)

    cycle_1 = [vertex_1]
    cycle_2 = [vertex_2]

    for i in range(numbers - 2):
        minimum_1 = np.amax(m)
        for v_1 in cycle_1:
            for r in remaining:
                if minimum_1 > m[v_1][r]:
                    minimum_1 = m[v_1][r]
                    closest_r_1 = r
                    closest_v_1 = v_1

        minimum_2 = np.amax(m)
        for v_2 in cycle_2:
            for r in remaining:
                if minimum_2 > m[v_2][r]:
                    minimum_2 = m[v_2][r]
                    closest_r_2 = r
                    closest_v_2 = v_2

        if len(cycle_1) < numbers / 2:
            if len(cycle_2) < numbers / 2:
                if minimum_1 < minimum_2:
                    cycle_1.insert(cycle_1.index(closest_v_1) + 1, closest_r_1)
                    remaining.remove(closest_r_1)
                else:
                    cycle_2.insert(cycle_2.index(closest_v_2) + 1, closest_r_2)
                    remaining.remove(closest_r_2)
            else:
                cycle_1.insert(cycle_1.index(closest_v_1) + 1, closest_r_1)
                remaining.remove(closest_r_1)
        else:
            cycle_2.insert(cycle_2.index(closest_v_2) + 1, closest_r_2)
            remaining.remove(closest_r_2)

    return cycle_1, cycle_2