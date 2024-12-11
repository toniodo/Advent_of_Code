"""Day 4 AoC  2024"""
from dataclasses import dataclass
from utils.parse import simple_parse

@dataclass
class Grid:
    """A class to represents grid"""
    data:list[list[str]]
    max_x: int
    max_y: int

def check_horizontally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x][y + id] != letter:
            return False
    return True

def check_back_horizontally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x][y - id] != letter:
            return False
    return True

def check_vertically(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x + id][y] != letter:
            return False
    return True

def check_back_vertically(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x - id][y] != letter:
            return False
    return True

def check_diagonally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x + id][y + id] != letter:
            return False
    return True

def check_back_diagonally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x - id][y - id] != letter:
            return False
    return True

def check_counter_diagonally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x - id][y + id] != letter:
            return False
    return True

def check_back_counter_diagonally(pos: tuple[int,int], grid:Grid):
    word = "XMAS"
    x,y = pos
    for id, letter in enumerate(word):
        if grid.data[x + id][y - id] != letter:
            return False
    return True


def count_xmas(pos: tuple[int,int], grid:Grid) -> int:
    number_xmas = 0
    x, y = pos
    # Horizontal
    if y < grid.max_y - 3 and check_horizontally(pos, grid):
        number_xmas += 1
    if y >= 3 and check_back_horizontally(pos, grid):
        number_xmas += 1
    # Vertical
    if x < grid.max_x - 3 and check_vertically(pos, grid):
        number_xmas += 1
    if x >= 3 and check_back_vertically(pos, grid):
        number_xmas += 1
    # Diagonal
    if x < grid.max_x - 3 and y < grid.max_y - 3 and check_diagonally(pos, grid):
        number_xmas += 1
    if x >= 3 and y >=3 and check_back_diagonally(pos, grid):
        number_xmas += 1
    # Counter Diagonal
    if x >= 3 and y < grid.max_y - 3 and check_counter_diagonally(pos, grid):
        number_xmas += 1
    if x < grid.max_x - 3 and y >=3 and check_back_counter_diagonally(pos, grid):
        number_xmas += 1
    return number_xmas

def count_all_xmas(grid: Grid):
    total_xmas = 0
    for x in range(grid.max_x):
        for y in range(grid.max_y):
            if grid.data[x][y] == "X":
                total_xmas += count_xmas((x,y), grid)
    print("The total number of XMAS is", total_xmas)
    return total_xmas

def check_mas(pos: tuple[int,int], grid:Grid):
    x, y = pos
    if grid.data[x-1][y-1] == "M" and grid.data[x+1][y-1] == "M" and grid.data[x+1][y+1] == "S" and grid.data[x-1][y+1] == "S":
        return True
    if grid.data[x+1][y-1] == "M" and grid.data[x+1][y+1] == "M" and grid.data[x-1][y+1] == "S" and grid.data[x-1][y-1] == "S":
        return True
    if grid.data[x+1][y+1] == "M" and grid.data[x-1][y+1] == "M" and grid.data[x-1][y-1] == "S" and grid.data[x+1][y-1] == "S":
        return True
    if grid.data[x-1][y+1] == "M" and grid.data[x-1][y-1] == "M" and grid.data[x+1][y-1] == "S" and grid.data[x+1][y+1] == "S":
        return True
    return False

def count_all_mas(grid: Grid):
    total_mas = 0
    for x in range(grid.max_x)[1:-1]:
        for y in range(grid.max_y)[1:-1]:
            if grid.data[x][y] == "A" and check_mas((x,y), grid):
                total_mas += 1
    print("The total number of XMAS is", total_mas)
    return total_mas

if __name__ == '__main__':
    # Create Grid
    all_lines = simple_parse("inputs/4.txt")
    grid_xmas = Grid(all_lines, len(all_lines), len(all_lines[0]))
    count_all_xmas(grid_xmas)
    count_all_mas(grid_xmas)
