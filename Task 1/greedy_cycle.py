import numpy as np
from sys import maxsize


def greedy_cycle(matrix, vertex_1):
    vertex_2 = np.argmax(matrix[vertex_1])
    max_cycle_size = len(matrix) / 2

    cycle_1 = []
    cycle_2 = []
    remaining = set(range(len(matrix)))

    insert_to_cycle(cycle_1, vertex_1, remaining)
    insert_to_cycle(cycle_2, vertex_2, remaining)

    while len(cycle_1) < max_cycle_size or len(cycle_2) < max_cycle_size:
        extend_cycle(matrix, cycle_1, remaining)
        extend_cycle(matrix, cycle_2, remaining)

    return cycle_1, cycle_2


def insert_to_cycle(cycle, vertex, remaining, location=0):
    cycle.insert(location, vertex)
    remaining.remove(vertex)


def calculate_extra_distance(cycle, new_vertex, location, matrix):
    vertex_1 = cycle[location-1]
    vertex_2 = cycle[location]
    return matrix[vertex_1][new_vertex] + matrix[new_vertex][vertex_2] - matrix[vertex_1][vertex_2]


def extend_cycle(matrix, cycle, remaining):
    min_extra_distance = maxsize
    best_vertex = 0
    best_location = 0

    for new_vertex in remaining:
        for location in range(len(cycle)):
            extra_distance = calculate_extra_distance(cycle, new_vertex, location, matrix)
            if extra_distance < min_extra_distance:
                min_extra_distance = extra_distance
                best_vertex = new_vertex
                best_location = location

    insert_to_cycle(cycle, best_vertex, remaining, best_location)
