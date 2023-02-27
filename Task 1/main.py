from create_matrix import *


def main():
    file_a = 'Graphs/kroA100.tsp.txt'
    file_b = 'Graphs/kroB100.tsp.txt'

    coordinates_a = read_data(file_a)
    matrix_a = build_matrix(coordinates_a)
    print(matrix_a)


if __name__ == '__main__':
    main()


