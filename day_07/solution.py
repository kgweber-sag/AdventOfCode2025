import argparse
import re
from collections import defaultdict

class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)
        self.beam_splits = 0
        self.beams = {}

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [x.strip() for x in file.readlines()]

        self.data = data

    def split_beam(self, col):
        self.beam_splits += 1
        return (col-1, col+1)
    

    def part_1(self):
        self.beams = {self.data.pop(0).index('S') : 1}
        lines = [line for line in self.data if '^' in line]
        splits = 0

        for row in lines:
            next_beams = defaultdict(int)

            for i, n  in self.beams.items():
                if row[i] == '^':
                    splits += 1
                    next_beams[i-1] += n
                    next_beams[i+1] += n
                else:
                    next_beams[i] += n

            self.beams = next_beams

        return self.beam_splits
        

    def part_2(self):
        return sum(self.beams.values())


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
