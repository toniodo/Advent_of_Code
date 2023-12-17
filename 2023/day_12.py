"""This is day 12 of advent of code 2023"""
from functools import lru_cache
from more_itertools import distinct_permutations
from tqdm import tqdm
from utils.file import list_lines

with open(file="inputs/day_12.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


def valid(input_test: str, nb_order: list[int]) -> bool:
    """Check if a given string respect every constraint"""
    input_parts = filter(lambda x: x != '', input_test.split('.'))
    input_lengths = list(map(len, input_parts))
    return input_lengths == nb_order


@lru_cache(maxsize=None)
def count_possible_solutions(line: str):
    """Count every possible solutions"""
    parts = line.split(' ')
    str_to_complete = parts[0]
    number_present_hash = len(list(filter(lambda x: x == '#', str_to_complete)))
    order_wanted = list(map(int, parts[1].split(',')))
    position_symbol = [ind for ind, symbol in enumerate(str_to_complete) if symbol == '?']
    nb_hash_to_add = sum(order_wanted) - number_present_hash
    nb_point_to_add = len(position_symbol) - nb_hash_to_add
    count = 0
    # Keep only distinct elements
    all_permutations = distinct_permutations("#" * nb_hash_to_add + "." * nb_point_to_add)
    for permutation in all_permutations:
        # Build the new string
        new_string = list(str_to_complete)
        for ind, pos in enumerate(position_symbol):
            new_string[pos] = permutation[ind]
        new_string = "".join(new_string)
        if valid(new_string, order_wanted):
            count += 1
    return count

# Using cache
@lru_cache(maxsize=None)
def num_solutions(string: str, count):
    """Return the number of possible solution using recursion"""
    string = string.lstrip('.')  # go to the first # or ?

    # Limit conditions
    if string == '':
        # Check if all the count have been used
        return int(len(count) == 0)

    if len(count) == 0:
        # Check if there is a remaining #
        return int(string.find('#') == -1)

    # If it starts with # we have to verify the first count
    if string[0] == '#':
        # Check if the count fits in the string (too short, or too many dots)
        if len(string) < count[0] or '.' in string[:count[0]]:
            return 0
        # If the string perfectly fits with the first count
        if len(string) == count[0]:
            # count has to be one
            return int(len(count) == 1)
        # No separation between groups
        if string[count[0]] == '#':
            return 0
        # Continue for the next group
        return num_solutions(string[count[0] + 1:], count[1:])

    # We try the possibilites for ? to be # or .
    return num_solutions('#' + string[1:], count) + num_solutions(string[1:], count)


def duplicate(lines: list[str], nb: int = 5):
    """Duplicate a sequence a given time"""
    new_lines = []
    for line in lines:
        sequence, nb_order = line.split(' ')
        init_sequence = sequence
        init_number = nb_order
        for _ in range(nb - 1):
            sequence = sequence + '?' + init_sequence
            nb_order = nb_order + ',' + init_number
        new_lines.append(sequence + ' ' + nb_order)
    return new_lines


def part_1(all_lines_file):
    """Print and return the solution for part 1"""
    global_count = 0
    for line in tqdm(all_lines_file):
        global_count += count_possible_solutions(line)
    print(f"The sum of all the counts is {global_count}")
    return global_count


def part_2(lines: list[str]):
    """Print the result for part 2"""
    new_lines = duplicate(lines, 5)
    global_count = 0
    for line in tqdm(new_lines):
        part = line.split(' ')
        order_wanted = tuple(map(int, part[1].split(',')))
        global_count += num_solutions(part[0], order_wanted)
    print(f"The sum of all the counts duplicated is {global_count}")

# Part 1
part_1(all_lines)

# Part 2
part_2(all_lines)
