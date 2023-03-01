import random as rn
import numpy as np
from draw_graph import draw_graph


def greedy_closest_neighbour(m):
    numbers = 100
    m = list(np.array(m)[:numbers, :numbers])
    # node_coords = node_coords[:numbers]

    nums = list(range(numbers))
    vertex1 = rn.choice(nums)
    nums.remove(vertex1)
    vertex2 = rn.choice(nums)
    vertex2 = np.argmax(m[vertex1])
    visited_value = np.amax(m) + 1
    for i in range(len(m)):
        m[i][i] = visited_value

    # cycle1 = [node_coords[vertex1]]
    # cycle2 = [node_coords[vertex2]]
    cycle1 = [vertex1]
    cycle2 = [vertex2]

    length1 = 0
    length2 = 0

    for i in range(numbers-2):
        for j in range(numbers):
            m[j][vertex1] = visited_value
            m[j][vertex2] = visited_value

        min1 = min(m[vertex1])
        min2 = min(m[vertex2])

        if len(cycle1) < numbers/2:
            if len(cycle2) < numbers/2:
                if min1 < min2:
                    vertex1 = np.argmin(m[vertex1])
                    cycle1.append(vertex1)
                    length1 += min1
                else:
                    vertex2 = np.argmin(m[vertex2])
                    cycle2.append(vertex2)
                    length2 += min2
            else:
                vertex1 = np.argmin(m[vertex1])
                cycle1.append(vertex1)
                length1 += min1
        else:
            vertex2 = np.argmin(m[vertex2])
            cycle2.append(vertex2)
            length2 += min2

    # length1 += round(((cycle1[0][0] - cycle1[-1][0])**2 + (cycle1[0][1] - cycle1[-1][1])**2)**(1/2))
    # length2 += round(((cycle2[0][0] - cycle2[-1][0])**2 + (cycle2[0][1] - cycle2[-1][1])**2)**(1/2))

    length1 += round(m[cycle1[0]][cycle1[-1]])
    length2 += round(m[cycle2[0]][cycle2[-1]])

    print(length1, length2)
    return cycle1, cycle2
    # draw_graph(node_coords, cycle1[0], cycle2[0], cycle1, cycle2, 'Greedy nearest neighbour')
