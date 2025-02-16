from aoc24.utils import read_lines_from_file, print_day_solution

import re

INPUT_FILE_PATH = "aoc24/day3/input.txt"
REGEX_STRING = r"mul\((\d\d\d|\d\d|\d),(\d\d\d|\d\d|\d)\)"


def part1():
    lines = read_lines_from_file(INPUT_FILE_PATH)
    res = 0

    for line in lines:
        mul_instructions = [
            (int(numbers[0]), int(numbers[1]))
            for numbers in re.findall(REGEX_STRING, line)
        ]

        for mul_instruction in mul_instructions:
            X, Y = mul_instruction
            res += X * Y

    print_day_solution(1, res)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
