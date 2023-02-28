from greedy_cycle import *


def main(file):
    coordinates = read_data(file)
    matrix = build_matrix(coordinates)
    greedy_cycle_method(coordinates, matrix)


if __name__ == '__main__':
    file_a = 'Graphs/kroA100.tsp.txt'
    file_b = 'Graphs/kroB100.tsp.txt'

    main(file_a)
    main(file_b)


