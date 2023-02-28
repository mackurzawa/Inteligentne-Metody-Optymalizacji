import random
import numpy as np
from sys import maxsize
from copy import deepcopy

from draw_graph import *
from create_matrix import *


def greedy_cycle_method(node_coords, distance_matrix):
    first_node_index = random.randint(0, len(distance_matrix)-1)
    first_node = node_coords[first_node_index]

    second_node_index = np.argmax(distance_matrix[first_node_index])
    second_node = node_coords[second_node_index]

    max_cycle_size = len(distance_matrix) / 2
    node_coords_copy = deepcopy(node_coords)

    cycle_1 = []
    cycle_2 = []

    insert_to_cycle(first_node_index, cycle_1, node_coords_copy)
    insert_to_cycle(second_node_index, cycle_2, node_coords_copy)

    while len(cycle_1) < max_cycle_size or len(cycle_2) < max_cycle_size:
        if len(cycle_1) < max_cycle_size:
            closest_node_index = find_closest_node_to_cycle(cycle_1, node_coords_copy)
            insert_to_cycle(closest_node_index, cycle_1, node_coords_copy)

        if len(cycle_2) < max_cycle_size:
            closest_node_index = find_closest_node_to_cycle(cycle_2, node_coords_copy)
            insert_to_cycle(closest_node_index, cycle_2, node_coords_copy)

    draw_graph(node_coords, first_node, second_node, cycle_1, cycle_2, 'Greedy cycle')


def find_closest_node_to_cycle(cycle, coordinates):
    cycle_center = get_center_of_the_cycle(cycle)
    min_distance = maxsize
    closest_node_index = 0
    for i, point in enumerate(coordinates):
        if point is not None:
            distance = calculate_distance(cycle_center, point)
            if distance < min_distance:
                min_distance = distance
                closest_node_index = i

    return closest_node_index


def get_center_of_the_cycle(cycle):
    return round(sum([x for x, _ in cycle])/len(cycle)), round(sum([y for _, y in cycle])/len(cycle))


def insert_to_cycle(new_node_index, cycle, coords):
    new_node = coords[new_node_index]
    min_extra_distance = maxsize
    best_location = 0
    for i in range(len(cycle)):
        #  mozna z macierzy brać pierwszy distance jak bysmy przechowywali gdzies id punktu
        #  TODO: zaimplementować punkt jako klasę(?)
        if i == len(cycle) - 1:
            current_distance = calculate_distance(cycle[i], cycle[0])
            new_distance = calculate_distance(cycle[i], new_node) + calculate_distance(new_node, cycle[0])
        else:
            current_distance = calculate_distance(cycle[i], cycle[i+1])
            new_distance = calculate_distance(cycle[i], new_node) + calculate_distance(new_node, cycle[i+1])

        extra_distance = new_distance - current_distance
        if extra_distance < min_extra_distance:
            min_extra_distance = extra_distance
            best_location = i + 1

    cycle.insert(best_location, new_node)
    coords[new_node_index] = None

