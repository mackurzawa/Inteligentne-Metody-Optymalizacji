import numpy as np

import greedy_cycle
import greedy_closest_neighbour
import draw_graph
import greedy_regret
from create_matrix import *


def calculate_cycles_length(matrix, cycle_1_closest_neighbour, cycle_2_closest_neighbour):
    cycle_1_closest_neighbour.append(cycle_1_closest_neighbour[0])
    cycle_2_closest_neighbour.append(cycle_2_closest_neighbour[0])

    length = 0
    for i in range(len(cycle_1_closest_neighbour) - 1):
        length += matrix[cycle_1_closest_neighbour[i]][cycle_1_closest_neighbour[i + 1]]
        length += matrix[cycle_2_closest_neighbour[i]][cycle_2_closest_neighbour[i + 1]]
    return length


def main(file):
    coordinates = read_data(file)
    matrix = build_matrix(coordinates)

    neighbour_lengths = []
    cycle_lengths = []
    regret_lengths = []
    for starting_vertex in range(100):
        cycle_1_closest_neighbour, cycle_2_closest_neighbour = greedy_closest_neighbour.greedy_closest_neighbour(matrix, starting_vertex)

        # Function that returns two cycles (first != last) using cycles method
        cycle_1_cycle, cycle_2_cycle = greedy_cycle.greedy_cycle(matrix, starting_vertex)

        # Function that returns two cycles (first != last) using regret method
        cycle_1_regret, cycle_2_regret = greedy_regret.greedy_regret(matrix, starting_vertex)

        neighbour_length = calculate_cycles_length(matrix, cycle_1_closest_neighbour, cycle_2_closest_neighbour)
        neighbour_lengths.append(neighbour_length)

        # Uncomment when cycles ready
        cycle_length = calculate_cycles_length(matrix, cycle_1_cycle, cycle_2_cycle)
        cycle_lengths.append(cycle_length)

        # Uncomment when regret ready
        regret_length = calculate_cycles_length(matrix, cycle_1_regret, cycle_2_regret)
        regret_lengths.append(regret_length)


    print(f"Nearest Neighbour min, avg, max for {file}")
    print(min(neighbour_lengths), sum(neighbour_lengths) / len(neighbour_lengths), max(neighbour_lengths))
    cycle_1_closest_neighbour, cycle_2_closest_neighbour = greedy_closest_neighbour.greedy_closest_neighbour(matrix, np.argmin(neighbour_lengths))
    draw_graph.draw_graph(coordinates, cycle_1_closest_neighbour[0], cycle_2_closest_neighbour[0], cycle_1_closest_neighbour, cycle_2_closest_neighbour, 'Greedy nearest neighbour')


    # Uncomment when cycles ready

    print(f"Cycles method min, avg, max for {file}")
    print(min(cycle_lengths), sum(cycle_lengths) / len(cycle_lengths), max(cycle_lengths))
    cycle_1_cycle, cycle_2_cycle = greedy_cycle.greedy_cycle(matrix, np.argmin(cycle_lengths))
    draw_graph.draw_graph(coordinates, cycle_1_cycle[0], cycle_2_cycle[0], cycle_1_cycle, cycle_2_cycle, 'Greedy cycles method')


    # Uncomment when regret ready

    print(f"Regret method min, avg, max for {file}")
    print(min(regret_lengths), sum(regret_lengths) / len(regret_lengths), max(regret_lengths))
    cycle_1_regret, cycle_2_regret = greedy_regret.greedy_regret(matrix, np.argmin(regret_lengths))
    draw_graph.draw_graph(coordinates, cycle_1_regret[0], cycle_2_regret[0], cycle_1_regret, cycle_2_regret, 'Greedy regret method')


if __name__ == '__main__':
    file_a = 'Graphs/kroA100.tsp.txt'
    file_b = 'Graphs/kroB100.tsp.txt'

    main(file_a)
    main(file_b)
