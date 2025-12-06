import argparse
from collections import defaultdict
from pprint import pprint

class Solver:
    def __init__(self, file_path=None):
        self.roll_positions = defaultdict(int)
        self.rolls_removed = 0
        self.load_data(file_path)
        self.count_all_paper_rolls()

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [list(x.strip()) for x in file.readlines()]

        self.data = data

    def count_all_paper_rolls(self):
        # get the paper roll counts
        for row_idx, row in enumerate(self.data):
            for col_idx, val in enumerate(row):
                if val == "@":
                    self.count_adjacent_paper_rolls(row_idx, col_idx)

    def is_on_grid(self, row, col):
        if 0 <= row < len(self.data) and 0 <= col < len(self.data[0]):
            return True
        return False

    def count_adjacent_paper_rolls(self, row, col):
        self.roll_positions[(row, col)] = 0
        for r in row - 1, row, row + 1:
            for c in col - 1, col, col + 1:
                if self.is_on_grid(r, c) and not (r == row and c == col):
                    if self.data[r][c] == "@":
                        self.roll_positions[(row, col)] += 1

    def print_debug(self):
        debug_data = self.data.copy()
        for (row, col), count in self.roll_positions.items():
            debug_data[row][col] = str(count)
        pprint(["".join(x) for x in debug_data])

    def part_1(self):
        return sum([1 for v in self.roll_positions.values() if v < 4])

    def part_2(self):
        iter_removed = -1
        while iter_removed !=0:
            to_remove = [pos for pos, count in self.roll_positions.items() if count < 4]
            iter_removed = len(to_remove)
            self.rolls_removed += iter_removed
            for pos in to_remove:
                self.data[pos[0]][pos[1]] = "."
                del self.roll_positions[pos]
            self.count_all_paper_rolls()
        # self.print_debug()
        return self.rolls_removed


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
