import argparse
from collections import defaultdict


class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [x.strip() for x in file.readlines()]

        self.data = data

    def part_1(self):
        pass

    def part_2(self):
        pass


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
