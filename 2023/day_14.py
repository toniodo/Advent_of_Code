"""This is day 14 of advent of code 2023"""
from collections import Counter
from copy import deepcopy
from utils.file import list_lines

with open(file="inputs/day_14.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


class Platform:
    """A class to represent a platform"""

    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])
        self.modified_grid = deepcopy(self.grid)
        self.rocks_pos = set()
        self.round_pos = []
        for i, row in enumerate(self.grid):
            for j in range(len(row)):
                symbol = self.grid[i][j]
                if symbol == '#':
                    self.rocks_pos.add((i, j))

    @property
    def load(self):
        """Compute the value of the load"""
        count = 0
        for i, row in enumerate(self.modified_grid):
            counter = Counter(row)
            count += counter['O'] * (self.n_rows - i)
        return count

    def actualize_pos(self):
        """Update the list of position of round rocks"""
        new_round = []
        for i, row in enumerate(self.modified_grid):
            for j in range(len(row)):
                symbol = self.modified_grid[i][j]
                if symbol == 'O':
                    new_round.append((i, j))
        return new_round

    def tilt_north(self):
        """Compute the tilt north of the platform"""
        self.round_pos = self.actualize_pos()
        for round_rock in self.round_pos:
            x, y = round_rock
            if x != 0 and self.modified_grid[x - 1][y] == '.':
                i = 1
                while x - i != -1 and self.modified_grid[x - i][y] == '.':
                    self.modified_grid[x - i + 1][y] = '.'
                    self.modified_grid[x - i][y] = 'O'
                    i += 1
        return self.modified_grid

    def tilt_west(self):
        """Compute the tilt west of the platform"""
        self.round_pos = self.actualize_pos()
        for round_rock in self.round_pos:
            x, y = round_rock
            if y != 0 and self.modified_grid[x][y - 1] == '.':
                i = 1
                while y - i != -1 and self.modified_grid[x][y - i] == '.':
                    self.modified_grid[x][y - i + 1] = '.'
                    self.modified_grid[x][y - i] = 'O'
                    i += 1
        return self.modified_grid

    def tilt_south(self):
        """Compute the tilt south of the platform"""
        self.round_pos = self.actualize_pos()
        for round_rock in self.round_pos[::-1]:
            x, y = round_rock
            if x != self.n_rows - 1 and self.modified_grid[x + 1][y] == '.':
                i = 1
                while x + i != self.n_rows and self.modified_grid[x + i][y] == '.':
                    self.modified_grid[x + i - 1][y] = '.'
                    self.modified_grid[x + i][y] = 'O'
                    i += 1
        return self.modified_grid

    def tilt_east(self):
        """Compute the tilt east of the platform"""
        self.round_pos = self.actualize_pos()
        for round_rock in self.round_pos[::-1]:
            x, y = round_rock
            if y != self.n_cols - 1 and self.modified_grid[x][y + 1] == '.':
                i = 1
                while y + i != self.n_cols and self.modified_grid[x][y + i] == '.':
                    self.modified_grid[x][y + i - 1] = '.'
                    self.modified_grid[x][y+i] = 'O'
                    i += 1
        return self.modified_grid

    def nb_cycle(self):
        """Determine period"""
        # Reset
        self.modified_grid = deepcopy(self.grid)
        cache_state = []
        new_list = deepcopy(self.modified_grid)
        cache_state.append(new_list)
        count = 0
        while True:
            self.tilt_north()
            self.tilt_west()
            self.tilt_south()
            new_list = deepcopy(self.tilt_east())
            count += 1
            if new_list in cache_state:
                ind_cache = cache_state.index(new_list)
                break
            cache_state.append(new_list)
        return ind_cache, count - ind_cache

    def cycle(self, n=1):
        """Perform a cycle"""
        self.modified_grid = deepcopy(self.grid)
        for _ in range(n):
            self.tilt_north()
            self.tilt_west()
            self.tilt_south()
            self.tilt_east()


platform_part1 = Platform(all_lines)
platform_part1.tilt_north()

print(f"The load after the tilt is {platform_part1.load}")

platform_part2 = Platform(all_lines)

cache_ind, period = platform_part2.nb_cycle()
print(f"The number of cycle is : {period} after {cache_ind} cycles")

platform_part2.cycle(((1000_000_000-cache_ind) % period) +cache_ind)
#platform_part2.cycle(3)
print(f"The final number of load is : {platform_part2.load}")
