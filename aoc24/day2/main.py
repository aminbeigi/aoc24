from aoc24.utils import read_lines_from_file, print_day_solution

INPUT_FILE_PATH = "./aoc24/day2/input.txt"
VALID_INCREASING_DIFFS = [1, 2, 3]
VALID_DECREASING_DIFFS = [-1, -2, -3]

def is_valid_increasing_report(report: list[int]) -> bool:
    for i in range(1, len(report)):
        current = report[i]
        prev = report[i - 1]
        diff = current - prev

        if diff not in VALID_INCREASING_DIFFS:
            return False
    return True

def is_valid_decreasing_report(report: list[int]) -> bool:
    for i in range(1, len(report)):
        current = report[i]
        prev = report[i - 1]
        diff = current - prev

        if diff not in VALID_DECREASING_DIFFS:
            return False
    return True

def is_safe_report(report: list[int]) -> bool:
    return is_valid_increasing_report(report) or is_valid_decreasing_report(report)

def is_safe_with_dampener(report: list[int]) -> bool:
    """check if a report can be made safe by removing one level"""
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True
    return False

def day1() -> None:
    lines = read_lines_from_file(INPUT_FILE_PATH)

    res = 0
    for line in lines:
        report = [int(i) for i in line.split()]

        if is_safe_report(report):
            res += 1

    print_day_solution(1, res)


def day2() -> None:
    lines = read_lines_from_file(INPUT_FILE_PATH)

    res = 0
    for line in lines:
        report = [int(i) for i in line.split()]

        if is_safe_report(report) or is_safe_with_dampener(report):
            res += 1

    print_day_solution(2, res)


if __name__ == "__main__":
    day1()
    day2()
