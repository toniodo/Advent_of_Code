"""This is day 21 of advent of code 2023"""
from copy import deepcopy
from queue import Queue
import numpy as np
from scipy.interpolate import lagrange
from utils.file import list_lines

with open(file="inputs/day_21.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


grid = [[*line] for line in all_lines]
modified_grid = deepcopy(grid)


def deep_index(lst: list[list[str]], w: str):
    """Return the index of an element in a list of a list"""
    return [(i, sub.index(w)) for (i, sub) in enumerate(lst) if w in sub]


def possible_actions(array, pos):
    """Return the possible actions from a given position"""
    successors = set()
    x, y = pos
    n_rows = len(array)
    n_cols = len(array[0])
    if 0 <= x - 1 and array[x - 1][y] != '#':
        # Up
        successors.add((x - 1, y))
    if x + 1 <= n_rows - 1 and array[x + 1][y] != '#':
        # Down
        successors.add((x + 1, y))
    if y - 1 >= 0 and array[x][y - 1] != '#':
        # Left
        successors.add((x, y - 1))
    if y + 1 <= n_cols - 1 and array[x][y + 1] != '#':
        # Right
        successors.add((x, y + 1))
    return successors


def possible_extra_actions(array, pos, pav):
    """Return the possible actions from a given position"""
    successors = set()
    x, y = pos
    px, py = pav
    n_rows = len(array)
    n_cols = len(array[0])

    if x == 0 and array[n_rows - 1][y] != '#':
        # Up and change paving
        successors.add(((n_rows - 1, y), (px - 1, py)))
    if x > 0 and array[x - 1][y] != '#':
        # Up
        successors.add(((x - 1, y), (px, py)))
    if x == n_rows - 1 and array[0][y] != '#':
        # Down and change paving
        successors.add(((0, y), (px + 1, py)))
    if x < n_rows - 1 and array[x + 1][y] != '#':
        # Down
        successors.add(((x + 1, y), (px, py)))
    if y == 0 and array[x][n_cols - 1] != '#':
        # Left and paving
        successors.add(((x, n_cols - 1), (px, py - 1)))
    if y > 0 and array[x][y - 1] != '#':
        # Left
        successors.add(((x, y - 1), (px, py)))
    if y == n_cols - 1 and array[x][0] != '#':
        # Right and paving
        successors.add(((x, 0), (px, py + 1)))
    if y < n_cols - 1 and array[x][y + 1] != '#':
        # Right
        successors.add(((x, y + 1), (px, py)))
    return successors


def possible_locations(array, steps):
    """Return the total number of possibles locations from a given number of steps"""
    start_pos = deep_index(array, 'S')[0]
    new_positions = possible_actions(array, start_pos)
    for _ in range(steps - 1):
        final_positions = set()
        for pos in new_positions:
            new_pos = possible_actions(array, pos)
            final_positions |= new_pos
        new_positions = final_positions
    return len(new_positions)


def bfs(array, steps):
    """Compute BFS given a number of steps"""
    start_pos = deep_index(grid, 'S')[0]
    start_paving = (0, 0)  # coordinates of the current grid
    V = set()  # set for visited positions
    L = Queue()
    L.put((0, start_pos, start_paving))  # (depth, position, paving)
    possible_positions = 0  # count the number of possible positions
    # Check if the number of steps is an odd number
    odd = steps & 1

    while not L.empty():
        s_d, s, s_p = L.get()  # get the depth, position and paving (state)

        if s_d == steps + 1:
            # Stop the exploration
            break

        # Check is already visited
        if (s, s_p) in V:
            continue
        V.add((s, s_p))

        # Check the condition to count it
        if odd and s_d & 1 or not odd and (s_d + 1) & 1:
            possible_positions += 1

        # Add successors
        for pos, pav in possible_extra_actions(array, s, s_p):
            if (pos, pav) not in V:
                depth = s_d + 1
                L.put((depth, pos, pav))

    return possible_positions


# Part 1
print(f"The total numbers of possible locations is {possible_locations(modified_grid,64)}")

# Part 2
points = np.array([65, 196, 327])
values = []
for point in points:
    values.append(bfs(modified_grid, point))

# Convert to an array
values = np.array(values)

# Interpolate the points
polynome = lagrange(points, values)
possible_pos = polynome(26501365)

print(f"The number of possible locations with duplication is {possible_pos}")
