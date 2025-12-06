import argparse
import re


class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)
        self.pt_1_invalid_ids = []
        self.pt_2_invalid_ids = []

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
        data = [(int(y[0]), int(y[1])) for y in [x.split("-") for x in data.split(",")]]

        self.data = data

    def part_1(self):
        repeater_match = r"(\d+)\1{1}$"  # exactly one repeat
        generous_repeater_match = r"(\d+)\1+$"  # any number of repeats
        for id_range in self.data:
            for id in range(id_range[0], id_range[1] + 1):
                repeats = re.match(repeater_match, str(id))
                if repeats:
                    self.pt_1_invalid_ids.append(id)
                generous_repeats = re.match(generous_repeater_match, str(id))
                if generous_repeats:
                    self.pt_2_invalid_ids.append(id)
        return sum(self.pt_1_invalid_ids)

    def part_2(self):
        # just let part 1 do the heavy lifting with the different regex
        return sum(self.pt_2_invalid_ids)


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
