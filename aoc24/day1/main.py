from aoc24.utils import read_lines_from_file, print_day_solution

INPUT_FILE_PATH = "./aoc24/day1/input.txt"


def day1() -> None:
    list1: list[int] = []
    list2: list[int] = []

    lines = read_lines_from_file(INPUT_FILE_PATH)

    for line in lines:
        value1, value2 = line.strip().split()
        list1.append(int(value1))
        list2.append(int(value2))

    list1.sort()
    list2.sort()

    res = 0

    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])

    print_day_solution(1, res)


def day2() -> None:
    list1: list[int] = []
    list2: list[int] = []

    lines = read_lines_from_file(INPUT_FILE_PATH)
    for line in lines:
        value1, value2 = line.strip().split()
        list1.append(int(value1))
        list2.append(int(value2))

    res = 0

    for number in list1:
        res += number * list2.count(number)

    print_day_solution(2, res)


if __name__ == "__main__":
    day1()
    day2()
