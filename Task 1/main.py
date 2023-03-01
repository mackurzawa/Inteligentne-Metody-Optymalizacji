from greedy_cycle import *
import greedy_closest_neighbour


def main(file):
    coordinates = read_data(file)
    matrix = build_matrix(coordinates)

    # greedy_cycle_method(coordinates, matrix)

    cycle_1_closest_neighbour, cycle_2_closest_neighbour = greedy_closest_neighbour.greedy_closest_neighbour(matrix)
    draw_graph(coordinates, cycle_1_closest_neighbour[0], cycle_2_closest_neighbour[0], cycle_1_closest_neighbour, cycle_2_closest_neighbour, 'Greedy nearest neighbour')


if __name__ == '__main__':
    file_a = 'Graphs/kroA100.tsp.txt'
    file_b = 'Graphs/kroB100.tsp.txt'

    main(file_a)
    main(file_b)


