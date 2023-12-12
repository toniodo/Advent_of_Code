"""This is day 10 of advent of code 2023"""
from queue import PriorityQueue
from typing import List, Tuple
from collections import Counter
from utils.file import list_lines

with open(file="inputs/day_10.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


class Labyrinth:
    """ A class to represent the Labyrinth """

    def __init__(self, lines: List[str]):
        self.grid = [list(line) for line in lines]
        self.n_cols = len(self.grid[0])
        self.n_rows = len(self.grid)
        self.start = [(i, sub.index('S')) for (i, sub) in enumerate(self.grid) if 'S' in sub][0]
        self.distances = [[0] * self.n_cols for _ in range(self.n_rows)]
        self.enclosed = [[0] * self.n_cols for _ in range(self.n_rows)]

    def get_actions(self, state: Tuple[int, int]):
        """Get all possible actions from a given state"""
        x, y = state
        current_sign = self.grid[x][y]
        if current_sign == 'S':
            current_sign = 'J'
            # current_sign = 'F'
            self.grid[x][y] = current_sign
        new_states = []
        if current_sign == '|':
            # Up
            new_states.append((x - 1, y))
            # Down
            new_states.append((x + 1, y))
        elif current_sign == '-':
            # Left
            new_states.append((x, y - 1))
            # Right
            new_states.append((x, y + 1))
        elif current_sign == 'L':
            # Up
            new_states.append((x - 1, y))
            # Right
            new_states.append((x, y + 1))
        elif current_sign == 'J':
            # Up
            new_states.append((x - 1, y))
            # Left
            new_states.append((x, y - 1))
        elif current_sign == '7':
            # Left
            new_states.append((x, y - 1))
            # Down
            new_states.append((x + 1, y))
        elif current_sign == 'F':
            # Right
            new_states.append((x, y + 1))
            # Down
            new_states.append((x + 1, y))
        return new_states

    def update_distances(self, state, value):
        """Update the grid of distances"""
        self.distances[state[0]][state[1]] = value

    def get_max(self):
        """Get the maximum value of all distances"""
        return max(max(distance) for distance in self.distances)

    def separate_areas(self):
        """Separate areas according the loop"""
        for x in range(self.n_rows):
            for y in range(self.n_cols):
                if self.distances[x][y] == 0 and (x, y) != self.start:
                    if x == 0 or x == self.n_rows - 1 or y == 0 or y == self.n_cols - 1:
                        # Border
                        self.enclosed[x][y] = -1
                    elif self.enclosed[x - 1][y] != 0:
                        # Horizontal propagation
                        self.enclosed[x][y] = self.enclosed[x - 1][y]
                    elif self.enclosed[x][y - 1] != 0:
                        # Vertical propagation
                        self.enclosed[x][y] = self.enclosed[x][y - 1]
                    elif self.interior((x, y)):
                        # Inside the loop
                        self.enclosed[x][y] = 1
                    else:
                        # Outside the loop
                        self.enclosed[x][y] = -1

    def interior(self, point: Tuple[int, int]) -> bool:
        """ Check if a point is in the loop """
        count_left = 0
        count_right = 0
        px, py = point
        for x in range(0, px):
            if self.distances[x][py] != 0 and (x, py) != self.start:
                symbol = self.grid[x][py]
                if symbol in {'-', '7', 'J'}:
                    count_left += 1
                if symbol in {'-', 'L', 'F'}:
                    count_right += 1
        min_value = min(count_left, count_right)
        if min_value % 2 == 0:
            return False
        return True

    def count_in_out(self):
        """ Count inside and outside points"""
        count_elt = [Counter(elt) for elt in self.enclosed]
        count_plus = 0
        count_minus = 0
        for elt in count_elt:
            if -1 in elt.keys():
                count_minus += elt[-1]
            if 1 in elt.keys():
                count_plus += elt[1]
        return count_minus, count_plus


def uniform_cost(labyrinth: Labyrinth):
    """Implements the uniform cost search"""
    start = labyrinth.start
    fringe = PriorityQueue()
    fringe.put((0, start))
    labyrinth.update_distances(start, 0)
    while not fringe.empty():
        priority, state = fringe.get()
        possible_actions = labyrinth.get_actions(state)
        for action in possible_actions:
            # Check not visited neighboors
            if labyrinth.distances[action[0]][action[1]] == 0 and action != start:
                fringe.put((priority + 1, action))
                labyrinth.update_distances(action, priority + 1)
    return labyrinth

my_labyrinth = Labyrinth(all_lines)

# Part 1
updated_labyrinth = uniform_cost(my_labyrinth)
print(f"The max distance is : {updated_labyrinth.get_max()}")

# Part 2
updated_labyrinth.separate_areas()
outside, inside = updated_labyrinth.count_in_out()
print(f"Number elements outside : {outside}")
print(f"Number elements inside : {inside}")
