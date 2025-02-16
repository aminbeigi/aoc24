from aoc24.utils import read_lines_from_file, print_day_solution

import re

INPUT_FILE_PATH = "aoc24/day3/input.txt"


def part1():
    REGEX_STRING = r"mul\((\d\d\d|\d\d|\d),(\d\d\d|\d\d|\d)\)"
    res = 0
    lines = read_lines_from_file(INPUT_FILE_PATH)
    all_lines = "".join(lines)

    mul_instructions = [
        (int(numbers[0]), int(numbers[1]))
        for numbers in re.findall(REGEX_STRING, all_lines)
    ]

    for mul_instruction in mul_instructions:
        x, y = mul_instruction
        res += x * y

    print_day_solution(1, res)


def part2():
    MUL_REGEX_STRING = r"mul\((\d\d\d|\d\d|\d),(\d\d\d|\d\d|\d)\)"
    res = 0
    lines = read_lines_from_file(INPUT_FILE_PATH)
    all_lines = "".join(lines)
    enabled = True
    instructions = re.split(r"(\bdo\(\)|\bdon\'t\(\))", all_lines)

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            mul_matches = re.findall(MUL_REGEX_STRING, instruction)
            for match in mul_matches:
                x, y = int(match[0]), int(match[1])
                if enabled:
                    res += x * y

    print_day_solution(2, res)


if __name__ == "__main__":
    part1()
    part2()
