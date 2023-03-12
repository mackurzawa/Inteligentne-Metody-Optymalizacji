import plotly.graph_objects as go
from typing import List, Tuple


def split_coordinates(coords: List[Tuple]) -> (List, List):
    x_arr = [x for x, _ in coords]
    y_arr = [y for _, y in coords]
    return x_arr, y_arr


def draw_graph(node_coords, start_point_1, start_point_2, cycle_1, cycle_2, title):
    cycle_1.append(cycle_1[0])
    cycle_2.append(cycle_2[0])

    start_point_1 = node_coords[start_point_1]
    start_point_2 = node_coords[start_point_2]

    cycle_1 = [node_coords[cycle_1[i]] for i in range(len(cycle_1))]
    cycle_2 = [node_coords[cycle_2[i]] for i in range(len(cycle_2))]

    x_arr, y_arr = split_coordinates(node_coords)
    cycle_1_x, cycle_1_y = split_coordinates(cycle_1)
    cycle_2_x, cycle_2_y = split_coordinates(cycle_2)

    fig = go.Figure(data=[
        # go.Scatter(x=x_arr, y=y_arr, mode='markers', name='Wszystkie dane'),
        go.Scatter(x=[start_point_1[0]], y=[start_point_1[1]], marker=dict(size=10, color='red'),
                   name='Wierzchołek startowy 1'),
        go.Scatter(x=[start_point_2[0]], y=[start_point_2[1]], marker=dict(size=10, color='red'),
                   name='Wierzchołek startowy 2'),
        go.Scatter(x=cycle_1_x, y=cycle_1_y, mode='lines+markers', name='Cykl 1'),
        go.Scatter(x=cycle_2_x, y=cycle_2_y, mode='lines+markers', name='Cykl 2')
        ])

    fig.update_layout(title=title)
    fig.show()
