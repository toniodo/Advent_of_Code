""" This is day 1 of Advent of Code 2023 """
from typing import List, Tuple
from utils.file import list_lines

with open("inputs/day_1.txt", 'r', encoding="utf-8") as f:
    l = list_lines(f)


def part_1(lines: List[str]) -> None:
    """Function that solves part 1 from given lines of input"""
    def extract_int(string: str):
        """ Returns a list with all the digit from a string"""
        return [int(value) for value in string if value.isdigit()]

    list_int = list(map(extract_int, lines))
    true_digit_list = [10 * number[0] + number[-1] for number in list_int if len(number) != 0]
    print(f"Sum of all values : {sum(true_digit_list)}")


def part_2(lines: List[str]) -> None:
    """Function that solves part 2 from given lines of input"""
    # Dictionary to interpret string to int
    translation = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    def extract_int(string: str) -> List[Tuple[int, int]]:
        """ Returns a list with all the digit from a string
        (even if it is written in full letters) and their index"""
        int_values = [(pos, int(value)) for pos, value in enumerate(string) if value.isdigit()]
        return sorted(int_values)

    def search_int(string: str) -> List[Tuple[int, int]]:
        """Returns a list of all int in string written in full letter and their index"""
        letters_numbers = [value for value in translation if value in string]
        letter_indexes = set()
        for value in letters_numbers:
            # Search the first occurence and its index from the beginning
            letter_indexes.add((string.find(value), translation[value]))
            # Search the last occurence and its index from the end
            last_pos = string.rfind(value)
            if (last_pos, value) not in letter_indexes:
                letter_indexes.add((last_pos, translation[value]))
        return sorted(letter_indexes)

    def select_min_max(string: str):
        """Return the first and the last value of a string containing int (letter + number)"""
        # Typing and initialisation
        int_idx: List[int] = []
        int_val: List[int] = []
        letter_idx: List[int] = []
        letter_val: List[int] = []

        int_in_string: List[Tuple[int, int]] = extract_int(string)
        # Check if there is int in the string
        if len(int_in_string) != 0:
            int_idx, int_val = zip(*int_in_string)

        letter_in_string: List[Tuple[int, int]] = search_int(string)
        # Check if there is a number written in letters in the string
        if len(letter_in_string) != 0:
            letter_idx, letter_val = zip(*letter_in_string)

        if len(letter_idx) == 0:
            # Only int int the string
            return 10 * int_val[0] + int_val[-1]
        if len(int_idx) == 0:
            # Only number written in letters in the string
            return 10 * letter_val[0] + letter_val[-1]

        # First digit (minimum index found)
        if min(int_idx) < min(letter_idx):
            first_val = int_val[0]
        else:
            first_val = letter_val[0]
        # Last digit (last index found)
        if max(int_idx) > max(letter_idx):
            last_val = int_val[-1]
        else:
            last_val = letter_val[-1]
        return 10 * first_val + last_val

    list_final_int = list(map(select_min_max, lines))
    print(f"Part 2 : Sum of all values : {sum(list_final_int)}")


# Run part 1
part_1(l)

# Run part 2
part_2(l)
