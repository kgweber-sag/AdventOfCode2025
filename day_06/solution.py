import argparse
from collections import defaultdict
import re

class Solver:
    def __init__(self, file_path=None):
        self.load_data(file_path)

    def load_data(self, file_path):
        with open(file_path, "r") as file:
            data = file.readlines()

        self.operators = re.split(r"\s+", data[-1].strip())
        self.values = [[int(x) for x in re.split(r"\s+", row.strip())] for row in data[:-1]]
        self.original_data = data

    def operation(self, a, b, operator) -> int:
        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        else:
            raise ValueError(f"Unknown operator: {operator}")

    def part_1(self):
        operation_totals = 0
        for index, operator in enumerate(self.operators):
            problem_value = self.values[0][index]
            for row in self.values[1:]:
                problem_value = self.operation(problem_value, row[index], operator)
            operation_totals += problem_value

        return operation_totals

    def unpack_column(self, start_index, end_index):
        column_data = []
        for row in self.original_data[:-1]:
            column_data.append(row[start_index:end_index].strip('\n'))
        print(column_data)
        new_values = [[column_data[row_index][col_index] for row_index in range(len(column_data))] for col_index in range(len(column_data[0])-1, -1, -1)]
        new_values = [int("".join(row).strip()) for row in new_values]
        return new_values


    def part_2(self):
        # we must completely reparse the original data
        operator_positions = [m.start() for m in re.finditer(r"[\+\*]", self.original_data[-1])]
        operation_totals = 0

        for operator_index, operator_position in enumerate(operator_positions):
            start_index = operator_positions[operator_index]
            end_index = operator_positions[operator_index + 1] -1 if operator_index + 1 < len(operator_positions) else len(self.original_data[0])
            this_problem = self.unpack_column(start_index, end_index)
            problem_value = this_problem[0]
            for value in this_problem[1:]:
                problem_value = self.operation(problem_value, value, self.operators[operator_index])
            operation_totals += problem_value

        return operation_totals

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
