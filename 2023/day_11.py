"""This is day 11 of advent of code 2023"""
from itertools import combinations
import numpy as np
from utils.file import list_lines

with open(file="inputs/day_11.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

# Retrieve number of columns and rows
n_rows = len(all_lines)
n_cols = len(all_lines[0])

all_lines = [[*line] for line in all_lines]
np_lines = np.asarray(all_lines, dtype=str)

# Coordinates of all # symbols
hash_rows, hash_cols = np.nonzero(np_lines == '#')

to_expand_rows = []
to_expand_cols = []

# Rows to be expanded
for i in range(n_rows):
    if i not in hash_rows:
        to_expand_rows.append(i)

# Columns to be expanded
for j in range(n_cols):
    if j not in hash_cols:
        to_expand_cols.append(j)


def manhattan_dist(a: tuple, b: tuple):
    """Compute the manhattan distance"""
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def common_member(a, b):
    """Returns the number of common elements"""
    a_set = set(a)
    b_set = set(b)

    return len((a_set & b_set))


def compute_min_dist(nb_expansion):
    """Compute the minimum distance given a number of expansion"""
    all_hashtags_pos = tuple(zip(hash_rows, hash_cols))
    sum_all_lengths = 0
    for x, y in combinations(all_hashtags_pos, 2):
        dist = manhattan_dist(x, y)
        # expansion on rows
        lower_row = min(x[0], y[0])
        upper_row = max(x[0], y[0])
        nb_common_rows = common_member(range(lower_row + 1, upper_row), to_expand_rows)
        dist += nb_common_rows * (nb_expansion - 1)

        # expansion on cols
        lower_col = min(x[1], y[1])
        upper_col = max(x[1], y[1])
        nb_common_cols = common_member(range(lower_col + 1, upper_col), to_expand_cols)
        dist += nb_common_cols * (nb_expansion - 1)

        # Add to toal sum
        sum_all_lengths += dist

    print(f"All sum of shortest lengths is : {int(sum_all_lengths)}")

# Part 1
compute_min_dist(2)

# Part 2
compute_min_dist(1e6)
