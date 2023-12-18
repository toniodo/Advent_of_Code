"""This is day 18 of advent of code 2023"""
from utils.file import list_lines

with open(file="inputs/day_18.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

all_lines = [line.split(' ') for line in all_lines]


def get_new_point(current_point, direction, times):
    """Return the new edge according the direction"""
    x, y = current_point
    if direction in {'L', 2, '2'}:
        return x, y - times
    if direction in {'D', 1, '1'}:
        return x + times, y
    if direction in {'R', 0, '0'}:
        return x, y + times
    if direction in {'U', 3, '3'}:
        return x - times, y
    raise ValueError


def compute_area(points):
    """Using trapezoid formula to return the area"""
    area = 0
    for i, (x, y) in enumerate(points):
        if i != len(points) - 1:
            area += (y + points[i + 1][1]) * (x - points[i + 1][0])
        else:
            area += (y + points[0][1]) * (x - points[0][0])
    return abs(0.5 * area)


def part_1(lines):
    """Print the result of part 1"""
    # Store the position of all the edges
    all_points = [(0, 0)]
    # Number of boundary points
    nb_points_ext = 0
    for points in lines:
        # Retrieve last point
        x, y = all_points[-1]
        direction = points[0]
        times = int(points[1])
        new_point = get_new_point((x, y), direction, times)
        nb_points_ext += times
        all_points.append(new_point)

    # Pick's theorem to find the number of interior points
    nb_points_int = compute_area(all_points) + 1 - nb_points_ext / 2

    print(f"The total number of cubic meters is {int(nb_points_ext+nb_points_int)}")


def part_2(lines):
    """Print the result of part 2"""
    # Store the position of all the edges
    all_new_points = [(0, 0)]
    # Number of boundary points
    nb_new_points_ext = 0
    for points in lines:
        # Retrieve last point
        x, y = all_new_points[-1]
        # Last number is the direction
        direction = points[2][-2]
        # Written in hexadecimal
        times = int(points[2][2:-2], 16)
        new_point = get_new_point((x, y), direction, times)
        nb_new_points_ext += times
        all_new_points.append(new_point)

    # Pick's theorem to find the number of interior points
    nb_new_points_int = compute_area(all_new_points) + 1 - nb_new_points_ext / 2

    print(f"The total number of cubic meters is {int(nb_new_points_ext+nb_new_points_int)}")


# Run part 1
part_1(all_lines)

# Run part 2
part_2(all_lines)
