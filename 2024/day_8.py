"""Day 8 AoC 2024"""
from utils.parse import simple_parse
from itertools import combinations

all_lines = simple_parse("inputs/8.txt")

class Environnement:
    """A class to describe the grid with the guard"""
    def __init__(self, grid: list[str]):
        self.antennas: set[tuple[int, int]] = set()
        self.antinodes = set()
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        for x, line in enumerate(grid):
            for y, elt in enumerate(line):
                if elt != '.':
                    self.antennas.add((elt, (x, y)))

    def compute_pos_antinodes(self):
        """Compute all the antinodes and add them to the set"""
        for a1, a2 in combinations(self.antennas, 2):
            # Check if the two antennas are of the same type
            if a1[0] == a2[0]:
                x1, y1 = a1[1]
                x2, y2 = a2[1]
                # Compute the positions of the two antinodes
                dx, dy = x1 - x2, y1 - y2
                # Check the position of the antinodes
                if (x1 + dx, y1 + dy) == (x2, y2):
                    anti_1 = (x2 + dx, y2 + dy)
                    anti_2 = (x1 - dx, y1 - dy)
                else:
                    anti_1 = (x1 + dx, y1 + dy)
                    anti_2 = (x2 - dx, y2 - dy)
                # If the antinodes are in the limits of the grid add them
                if self.check_limit(anti_1):
                    self.antinodes.add(anti_1)
                if self.check_limit(anti_2):
                    self.antinodes.add(anti_2)


    def check_limit(self, pos):
        """Check if pos is in the limit of the grid"""
        x,y = pos
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def n_pos_antinodes(self):
        """Return the number of distinct postions of antinodes"""
        return len(self.antinodes)

    def compute_pos_extended_antinodes(self):
        """Compute all the antinodes and add them to the set"""
        for a1, a2 in combinations(self.antennas, 2):
            # Check if the two antennas are of the same type
            if a1[0] == a2[0]:
                x1, y1 = a1[1]
                x2, y2 = a2[1]
                # Antinodes of the antenna
                self.antinodes.add(a1[1])
                self.antinodes.add(a2[1])
                # Compute the positions of the two antinodes
                dx, dy = x1 - x2, y1 - y2
                # Check the position of the antinodes
                if (x1 + dx, y1 + dy) == (x2, y2):
                    anti_1 = (x2 + dx, y2 + dy)
                    anti_2 = (x1 - dx, y1 - dy)
                else:
                    anti_1 = (x1 + dx, y1 + dy)
                    anti_2 = (x2 - dx, y2 - dy)
                while self.check_limit(anti_1) or self.check_limit(anti_2):
                    # If the antinodes are in the limits of the grid add them
                    if self.check_limit(anti_1):
                        self.antinodes.add(anti_1)
                    if self.check_limit(anti_2):
                        self.antinodes.add(anti_2)
                    anti_1 = (anti_1[0] + dx, anti_1[1] + dy)
                    anti_2 = (anti_2[0] - dx, anti_2[1] - dy)

env = Environnement(all_lines)
env.compute_pos_antinodes()
print("The number of distinct positions for antinodes is", env.n_pos_antinodes())

env.compute_pos_extended_antinodes()
print("The number of distinct positions for antinodes is", env.n_pos_antinodes())
