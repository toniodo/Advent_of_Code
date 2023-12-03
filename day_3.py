""" This is day 3 of Advent of Code """
from math import sqrt
from typing import List, Tuple, Literal
from utils.file import list_lines
from utils.distance import euclidian_distance


def sort_number_symbols(lines: List[List[str]], specific_symbol: str | Literal["all"]
                        = "all") -> Tuple[set[Tuple[int, int, int]], set[Tuple[int, int]]]:
    """Returns a tuple with the a set of all numbers and thier respective position
    and set of all the position of a given symbol"""
    numbers = set()
    symbols = set()
    for i, line in enumerate(lines):
        shift: int = 0
        for j, elt in enumerate(line):
            # Check if the element is a number
            if elt.isnumeric():
                numbers.add((int(elt), i, j + shift))
                shift += len(elt)
            # Check if the element contains a number
            elif any(chr.isdigit() for chr in elt):
                hidden_number = ''
                # For all the member of the string the symbols is added or the number is rebuilt
                for digit in elt:
                    if digit.isdigit():
                        hidden_number += digit
                    elif hidden_number != '':
                        numbers.add((int(hidden_number), i, j + shift - len(hidden_number)))
                        hidden_number = ''
                        if specific_symbol in ('all', digit):
                            symbols.add((i, j + shift))
                    elif specific_symbol in ('all', digit):
                        symbols.add((i, j + shift))
                    shift += 1
                # The end of the string is only a number
                if hidden_number != '':
                    numbers.add((int(hidden_number), i, j + shift - len(hidden_number)))
                    hidden_number = ''

            elif elt != '':
                symbols.add((i, j + shift))
                shift += 1
    return numbers, symbols


def part_1(lines: List[List[str]]):
    """Returns the answer of part 1"""
    numbers, symbols = sort_number_symbols(lines)

    part_numbers = []
    for number in numbers:
        value, k, l = number
        n = len(str(value))
        added = False
        # Check for all digit if a symbol is at least one of the eight coordinates surrounding it
        for digit_shift in range(n):
            for symbol in symbols:
                if euclidian_distance((k, l + digit_shift), symbol) <= sqrt(2):
                    part_numbers.append(value)
                    added = True
                    break
            if added:
                break
    print(f"The sum of all not part numbers is: {sum(part_numbers)}")


def part_2(lines: List[List[str]]):
    """Solve part 2"""
    numbers, symbols = sort_number_symbols(lines, '*')

    gear_numbers = []
    for symbol in symbols:
        for number in numbers:
            value, i, j = number
            n = len(str(value))
            for digit_shift in range(n):
                if euclidian_distance((i, j + digit_shift), symbol) <= sqrt(2):
                    gear_numbers.append((value, *symbol))
                    break

    gear_ratio = 0
    for symbol in symbols:
        count = 0
        value_1 = 0
        value_2 = 0
        for gear in gear_numbers:
            if gear[1] == symbol[0] and gear[2] == symbol[1]:
                count += 1
                if value_1 != 0:
                    value_2 = gear[0]
                else:
                    value_1 = gear[0]
        if count == 2:
            gear_ratio += value_1 * value_2

    print(f"The sum of all gear ratios is: {gear_ratio}")


with open("inputs/day_3.txt", 'r', encoding='utf-8') as f:
    all_lines = list_lines(f)

all_lines = list(map(lambda x: x.split('.'), all_lines))

# Run part 1
part_1(all_lines)  # 519444

# Run part 2
part_2(all_lines)  # 74528807
