import math


def read_data(file):
    coordinates = []
    with open(file) as f:
        lines = f.read().split('\n')[6:-2]

        for line in lines:
            _, x, y = line.split()
            coordinates.append((int(x), int(y)))

    return coordinates


def calculate_distance(p1, p2):
    return round(math.dist(p1, p2))


def build_matrix(coordinates):
    matrix = [[0] * 100 for _ in range(len(coordinates))]
    for i, p1 in enumerate(coordinates):
        for j, p2 in enumerate(coordinates):
            matrix[i][j] = calculate_distance(p1, p2)

    return matrix


