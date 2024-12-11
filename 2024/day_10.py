"""Day 10 AoC 2024"""
from utils.parse import simple_parse
from collections import deque

all_lines = simple_parse("inputs/10.txt")


class TopologicalMap:
    """A class to represent a topological map"""

    def __init__(self, grid_values: list[int]):
        self.grid: list[list[int]] = [[int(val) for val in line] for line in grid_values]
        self.max_x = len(grid_values)
        self.max_y = len(grid_values[0])
        self.trailheads = set((x, y) for x, line in enumerate(self.grid)
                              for y, elt in enumerate(line) if elt == 0)

    def bfs(self, start_pos, extended: bool=False):
        """Perform BFS to find all the trailheads"""
        queue = deque()
        x, y = start_pos
        queue.appendleft((0, (x,y))) # value, pos
        pos_nine = set()
        count = 0
        while len(queue) != 0:
            value, pos = queue.pop()

            # Check if terminal
            if value == 9:
                if not extended and not pos in pos_nine:
                    pos_nine.add(pos)
                    count += 1
                elif extended:
                    pos_nine.add(pos)
                    count += 1
                continue

            for neighbour in self.neighbours(value, pos):
                # Append to the queue
                queue.appendleft(neighbour)
        return count

    def neighbours(self, value, pos):
        """Return all the neighbours given a position and value"""
        all_neighbours = set()
        x, y = pos
        if x > 0 and self.grid[x-1][y] - value == 1:
            # Go left
            all_neighbours.add((self.grid[x-1][y], (x-1, y)))
        if x < self.max_x-1 and self.grid[x+1][y] - value == 1:
            # Go right
            all_neighbours.add((self.grid[x+1][y], (x+1, y)))
        if y > 0 and self.grid[x][y-1] - value == 1:
            # Go up
            all_neighbours.add((self.grid[x][y-1], (x, y-1)))
        if y < self.max_y-1 and self.grid[x][y+1] - value == 1:
            # Go down
            all_neighbours.add((self.grid[x][y+1], (x, y+1)))
        return all_neighbours

    def update_nine(self, extended: bool = False):
        """Update all the nine reachable positions"""
        score_trailheads = 0
        for trailhead in self.trailheads:
            score_trailheads += self.bfs(trailhead, extended)
        return score_trailheads

top_map = TopologicalMap(all_lines)
print("The sum of all trailheads is", top_map.update_nine())

print("The sum of all trailheads paths is", top_map.update_nine(True))
