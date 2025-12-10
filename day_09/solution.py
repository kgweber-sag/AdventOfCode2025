import argparse
from itertools import combinations
import numpy as np
from shapely.geometry import Polygon, box
from shapely import plotting

class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [tuple([int(y) for y in x.strip().split(',')]) for x in file.readlines()]

        self.data = data
    def part_1(self):
        largest_area = 0
        for combo in combinations(self.data, 2):
            combo_area = (abs(combo[0][0] - combo[1][0]) + 1) * (abs(combo[0][1] - combo[1][1]) + 1)
            if combo_area > largest_area:
                largest_area = combo_area

        return largest_area


    def part_2(self):
        largest_contained_area = 0
        floor_polygon = Polygon(self.data)
        floor_bbox = box(*floor_polygon.bounds)
        for combo in combinations(self.data, 2):
            rect = box(min(combo[0][0], combo[1][0]), min(combo[0][1], combo[1][1]),
                       max(combo[0][0], combo[1][0]), max(combo[0][1], combo[1][1]))
            if not floor_bbox.covers(rect):
                continue
            if floor_polygon.covers(rect):
                combo_area = (abs(combo[0][0] - combo[1][0]) + 1) * (abs(combo[0][1] - combo[1][1]) + 1)
                if combo_area > largest_contained_area:
                    largest_contained_area = combo_area
        return largest_contained_area


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
    result_part_1 = day.part_1()
    result_part_2 = day.part_2()
    print(f"Part 1 Result: {result_part_1}")
    print(f"Part 2 Result: {result_part_2}")
