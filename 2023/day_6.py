"""This is day 6 of advent of code 2023"""
from functools import reduce
import numpy as np
from numpy.polynomial import Polynomial
from utils.file import list_lines

with open(file="inputs/day_6.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

all_lines = list(map(lambda x: x.split(" "), all_lines))


def part_1(lines: list[str]):
    """Prints the solution of part 1 with naive approach"""
    times = [int(x) for x in lines[0] if x.isnumeric()]
    distances = [int(x) for x in lines[1] if x.isnumeric()]

    possibilities = [0] * len(distances)

    for ind, distance in enumerate(distances):
        # Test for all the possible values
        for i in range(times[ind]):
            d = i * (times[ind] - i)
            if d >= distance:
                possibilities[ind] += 1

    all_possibilities = reduce(lambda a, b: a * b, possibilities)
    print(f"The number of possibilities is {all_possibilities}")


def part_2(lines: list[str]):
    """Prints the solution of part 2 with naive approach"""
    times = [x for x in lines[0] if x.isnumeric()]
    distances = [x for x in lines[1] if x.isnumeric()]
    # Concatenation
    time = int(reduce(lambda a, b: a + b, times))
    distance = int(reduce(lambda a, b: a + b, distances))
    possibilities = 0

    # Test for all the possible values
    for i in range(time):
        d = i * (time - i)
        if d >= distance:
            possibilities += 1
    print(f"The number of possibilities is {int(possibilities)}")


def part_1_faster(lines: list[str]):
    """Prints the solution of part 1 faster"""
    times = [int(x) for x in lines[0] if x.isnumeric()]
    distances = [int(x) for x in lines[1] if x.isnumeric()]

    possibilities = [0] * len(distances)

    for ind, (time, distance) in enumerate(zip(times, distances)):
        polynome = Polynomial((-distance, time, -1))
        d1, d2 = polynome.roots()
        new_d1 = np.ceil(d1)
        new_d2 = np.floor(d2)
        possibilities[ind] = new_d2 - new_d1 + 1
    all_possibilities = reduce(lambda a, b: a * b, possibilities)
    print(f"The number of possibilities is {int(all_possibilities)}")


def part_2_faster(lines: list[str]):
    """Prints the solution of part 2 faster"""
    times = [x for x in lines[0] if x.isnumeric()]
    distances = [x for x in lines[1] if x.isnumeric()]
    # Concatenation
    time = int(reduce(lambda a, b: a + b, times))
    distance = int(reduce(lambda a, b: a + b, distances))
    possibilities = 0

    polynome = Polynomial((-distance, time, -1))
    d1, d2 = polynome.roots()
    new_d1 = np.ceil(d1)
    new_d2 = np.floor(d2)
    possibilities = new_d2 - new_d1 + 1
    print(f"The number of possibilities is {int(possibilities)}")


# Run part 1
part_1_faster(all_lines)

# Run part 2
part_2_faster(all_lines)
