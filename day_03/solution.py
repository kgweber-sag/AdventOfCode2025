import argparse
from itertools import combinations


class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [x.strip() for x in file.readlines()]
        self.data = data

    def part_1(self):
        max_vals = []
        for line in self.data:
            combos = combinations(line, 2)
            vals = [int(a)*10 + int(b) for a, b in combos]
            max_vals.append(max(vals))

        return sum(max_vals)
    
    # combinations can't handle that many operations
    @staticmethod
    def find_max_val(bank, length):
        selected = []
        left = 0

        for right in range(len(bank) - length + 1, len(bank) + 1):
            left += bank[left:].index(max(bank[left:right])) + 1
            selected.append(bank[left - 1])

        return int("".join(selected))


    def part_2(self):
        part_2_sum = 0
        for line in self.data:
            part_2_sum += self.find_max_val(line, 12)

        return part_2_sum

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
