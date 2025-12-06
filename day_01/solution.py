import argparse
from collections import defaultdict


class solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)
        self.zero_landings = 0
        self.zero_touches = 0

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            self.data = [(x[0], int(x[1:].strip())) for x in file.readlines()]

    def part_1(self):
        initial_position = 50
        dial_size = 100
        position = initial_position

        for direction, steps in self.data:
            if direction == "R":
                position = (position + steps) % dial_size
            elif direction == "L":
                position = (position - steps) % dial_size
            if position == 0:
                self.zero_landings += 1
        return self.zero_landings

    def part_2(self):
        initial_position = 50
        dial_size = 100
        position = initial_position

        for direction, steps in self.data:

            zero_touches = 0
            if direction == "R":
                if position + steps > dial_size:
                    adjusted_delta = steps + position
                    zero_touches = adjusted_delta // dial_size
                position = (position + steps) % dial_size

            else:
                if position - steps < 0:
                    adjusted_delta = dial_size - position if position != 0 else 0
                    zero_touches = (steps + adjusted_delta) // dial_size
                position = (position - steps) % dial_size

            if position == 0 and steps < dial_size:
                zero_touches += 1
            self.zero_touches += abs(zero_touches)

            print(
                f"Direction: {direction}, Steps: {steps}, Position: {position}, Zero Touches: {abs(zero_touches)}, total zero touches: {self.zero_touches}"
            )
        return self.zero_touches


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    # bool to load test or real data
    args.add_argument("--real", action="store_true", help="Load real data")
    parsed_args = args.parse_args()

    if parsed_args.real:
        file = "run_data.txt"
    else:
        file = "test_data.txt"

    day = solver(file_path=file)
    result_part_1 = day.part_1()
    result_part_2 = day.part_2()
    print(f"Part 1 Result: {result_part_1}")
    print(f"Part 2 Result: {result_part_2}")
