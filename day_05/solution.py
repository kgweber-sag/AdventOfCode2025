import argparse


class Solver:
    def __init__(self, file_path=None):
        self.item_ids = set()
        self.ranges = []
        self.load_data(file_path)
        self.ranges.sort()

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = [x.strip() for x in file.readlines()]
        for line in data:
            if '-' in line:
                self.ranges.append([int(x) for x in line.split('-')])
            elif line == '':
                continue
            else:
                self.item_ids.add(int(line))
        self.data = data

    def part_1(self):
        fresh_id_count = 0
        for id in self.item_ids:
            for r in self.ranges:
                if r[0] <= id <= r[1]:
                    fresh_id_count += 1
                    break
        return fresh_id_count

    def part_2(self):
        fresh_id_count = 0
        previous_range = None
        for r in self.ranges:
            print(f"Processing range: {r}")
            if previous_range and r[0] <= previous_range[1]:
                r[0] = previous_range[1] + 1
            if r[0] > r[1]:
                continue
            else:
                fresh_id_count += r[1] - r[0] + 1
            previous_range = r
        return fresh_id_count


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
