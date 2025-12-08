import argparse
import numpy as np
from itertools import combinations
import networkx as nx

class Solver:
    def __init__(self, file_path=None):
        self.connection_count = 0
        self.load_data(file_path)
        self.calculate_distances()
        self.last_x_pair = (-1, -1)
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.data.keys())

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [x.strip().split(',') for x in file.readlines()]
        data = {ix: [int(y) for y in x] for ix, x in enumerate(data)}
        self.data = data

    def calculate_3d_linear_distance(self, coords1, coords2):
        return np.sqrt(
            (coords2[0] - coords1[0]) ** 2 +
            (coords2[1] - coords1[1]) ** 2 +
            (coords2[2] - coords1[2]) ** 2
        )

    def calculate_distances(self):
        self.distances = {}
        for (i, coord1), (j, coord2) in combinations(self.data.items(), 2):
            dist = self.calculate_3d_linear_distance(coord1, coord2)
            self.distances[dist] = (i, j)

    def part_1(self):
        print(len(self.distances))
        self.working_distances = sorted(self.distances.keys())
        for _ in range(self.connection_count):
                self.add_edge_from_distance()
        components = list(nx.connected_components(self.graph))
        return np.prod(sorted([len(c) for c in components], reverse=True)[0:3])

    def add_edge_from_distance(self):
        next_distance = self.working_distances[0]
        self.graph.add_edge(*self.distances[next_distance])
        self.last_x_pair = (
            self.data[self.distances[next_distance][0]][0],
            self.data[self.distances[next_distance][1]][0]
        )
        self.working_distances.pop(0)


    def part_2(self):
        while not nx.is_connected(self.graph):
            self.add_edge_from_distance()
        return self.last_x_pair[0] * self.last_x_pair[1]


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    # bool to load test or real data
    args.add_argument("--run", action="store_true", help="Load run data")
    parsed_args = args.parse_args()

    if parsed_args.run:
        file = "run_data.txt"
    else:
        file = "test_data.txt"

    day = Solver(file_path=file)
    day.connection_count = 1000 if parsed_args.run else 10
    result_part_1 = day.part_1()
    result_part_2 = day.part_2()
    print(f"Part 1 Result: {result_part_1}")
    print(f"Part 2 Result: {result_part_2}")
