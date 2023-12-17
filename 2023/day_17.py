"""This is day 17 of advent of code 2023"""
from queue import PriorityQueue
from utils.file import list_lines

with open(file="inputs/day_17.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


class CrucyPath:
    """A class to represent the problem"""

    def __init__(self, init_pos, end_pos, cost_grid):
        self.start = init_pos
        self.end = end_pos
        self.grid = cost_grid
        self.n_rows = len(self.grid)
        self.n_cols = len(self.grid[0])

    def isGoalState(self, pos):
        """Return if we arrive to the goal"""
        return pos == self.end
    
    def isGoalState_ultra(self, pos, times):
        """Return if we arrive to the goal with condition ultra"""
        return pos == self.end and times >= 4

    def getSuccessors(self, state_pos):
        """Return a set of all successors"""
        successors = set()
        x, y = state_pos
        for (di, dj) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            successors.add(((x + di, y + dj), (di, dj)))
        return successors


def ucs(problem: CrucyPath):
    """Search the node of least total cost first."""

    start = problem.start
    V = set()
    L = PriorityQueue()
    L.put((0, start, None, 0))

    while not L.empty():
        s_c, s, s_a, s_t = L.get()  # get the priority and position (state)

        # If already visited continue
        if (s, s_a, s_t) in V:
            continue

        V.add((s, s_a, s_t))

        if problem.isGoalState(s):
            # Return current cost
            return s_c

        for p, a in problem.getSuccessors(s):
            if not (0 <= p[0] < problem.n_rows and 0 <= p[1] < problem.n_cols) or (
                    (s_a is not None) and a[0] == -s_a[0] and a[1] == -s_a[1]):
                continue
            cost = s_c + problem.grid[p[0]][p[1]]
            # New inertia
            if s_a != a:
                new_t = 1
            else:
                new_t = s_t + 1
            # Check if in visited
            if (p, a, new_t) in V:
                continue
            # Check the inertia condition
            if new_t <= 3:
                L.put((cost, p, a, new_t))


def ucs_ultra(problem: CrucyPath):
    """Search the node of least total cost first."""

    start = problem.start
    V = set()
    L = PriorityQueue()
    L.put((0, start, None, 0))

    while not L.empty():
        s_c, s, s_a, s_t = L.get()  # get the priority and position (state)

        # If already visited continue
        if (s, s_a, s_t) in V:
            continue

        V.add((s, s_a, s_t))

        if problem.isGoalState_ultra(s, s_t):
            # Return current cost
            return s_c

        for p, a in problem.getSuccessors(s):
            if not (0 <= p[0] < problem.n_rows and 0 <= p[1] < problem.n_cols) or (
                    (s_a is not None) and a[0] == -s_a[0] and a[1] == -s_a[1]):
                continue
            cost = s_c + problem.grid[p[0]][p[1]]
            if s_a is not None and s_a != a and s_t < 4:
                continue
            new_t = s_t + 1
            if s_a != a and new_t >= 4:
                new_t = 1
            # Check if not 10 consecutives moves
            elif new_t > 10:
                continue
            # Check if in visited
            if (p, a, new_t) in V:
                continue
            L.put((cost, p, a, new_t))


list_costs = [list(map(int, line)) for line in all_lines]
my_problem = CrucyPath((0, 0), (len(list_costs) - 1, len(list_costs[0]) - 1), list_costs)

# Part 1
all_costs_path = ucs(my_problem)
print(f"The cost of the path of part 1 is {all_costs_path}")

# Part 2
all_costs_path = ucs_ultra(my_problem)
print(f"The cost of the path of part 2 is {all_costs_path}")
