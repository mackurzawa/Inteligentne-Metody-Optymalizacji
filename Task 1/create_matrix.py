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
    n = 100
    matrix = [[0] * n for _ in range(len(coordinates))]

    for i in range(n):
        for j in range(i+1, n):
            distance = calculate_distance(coordinates[i], coordinates[j])
            matrix[i][j] = distance
            matrix[j][i] = distance

    return matrix


