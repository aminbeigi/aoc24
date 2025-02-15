from colorama import Fore, init
from typing import Literal

init(autoreset=True)


def read_lines_from_file(file_path: str) -> list[str]:
    try:
        with open(file_path, "r") as file:
            lst = file.readlines()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    return lst


def print_day_solution(day: Literal[1, 2], result: int) -> None:
    """Prints a nicely formatted solution for a given day with color."""
    print(f"{Fore.GREEN}Day {day}: Solution")
    print(f"{Fore.BLUE}{'=' * 20}")
    print(f"{Fore.YELLOW}Result: {result}")
    print(f"{Fore.BLUE}{'=' * 20}\n")


def _private_func() -> None:
    return


__all__ = ["read_lines_from_file", "print_day_solution"]
