import numpy as np
from sys import maxsize


def greedy_cycle(matrix, vertex_1):
    vertex_2 = np.argmax(matrix[vertex_1])
    max_cycle_size = len(matrix) / 2

    cycle_1 = []
    cycle_2 = []
    visited = set()

    insert_to_cycle(cycle_1, vertex_1, visited)
    insert_to_cycle(cycle_2, vertex_2, visited)

    while len(cycle_1) < max_cycle_size or len(cycle_2) < max_cycle_size:
        extend_cycle(matrix, cycle_1, visited)
        extend_cycle(matrix, cycle_2, visited)

    return cycle_1, cycle_2


def insert_to_cycle(cycle, vertex, visited, location=0):
    cycle.insert(location, vertex)
    visited.add(vertex)


def extend_cycle(matrix, cycle, visited):
    min_extra_distance = maxsize
    best_vertex = 0
    best_location = 0

    for new_vertex in range(len(matrix)):
        if new_vertex not in visited:
            for cycle_index, cycle_vertex in enumerate(cycle):
                if cycle_index == len(cycle) - 1:
                    current_distance = matrix[cycle_vertex][cycle[0]]
                    new_distance = matrix[cycle_vertex][new_vertex] + matrix[new_vertex][cycle[0]]
                else:
                    current_distance = matrix[cycle_vertex][cycle[cycle_index+1]]
                    new_distance = matrix[cycle_vertex][new_vertex] + matrix[new_vertex][cycle[cycle_index+1]]

                extra_distance = new_distance - current_distance
                if extra_distance < min_extra_distance:
                    min_extra_distance = extra_distance
                    best_vertex = new_vertex
                    best_location = cycle_index + 1

    insert_to_cycle(cycle, best_vertex, visited, best_location)
