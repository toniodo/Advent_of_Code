"""Day 7 AoC 2024"""
from utils.parse import simple_parse
from collections import deque

all_lines = simple_parse("inputs/7.txt")

all_calibrations = []
for line in all_lines:
    line = line.split(": ")
    values = line[1].split(" ")
    values = list(map(int, values))
    all_calibrations.append((int(line[0]), values))

def dfs_calibration(calibration: tuple[int, list[int]], extended:bool = False):
    """Perform DFS to check if a valid calibration is possible"""
    fringe = deque()
    final_result = calibration[0]
    calibration_values = calibration[1]
    n_values = len(calibration_values)
    # Add the root node to the fringe in the format (index, cumulated value)
    fringe.append((0, calibration_values[0]))
    while len(fringe) != 0:
        # Retrieve the node
        current_id, current_result = fringe.pop()

        # Check if the node is terminal
        if current_id == n_values - 1:
            if current_result == final_result:
                return final_result
            if len(fringe) != 0:
                continue
            return 0

        # Compute the next values (Neighbours)
        next_value = calibration_values[current_id + 1]
        plus_value = current_result + next_value
        times_value = current_result * next_value
        # Add the concatenation operator
        if extended:
            concat_value = int(str(current_result) + str(next_value))

        # Only add the value to the fringe if they don't exceed the expected result (Pruning)
        if plus_value <= final_result:
            fringe.append((current_id + 1, plus_value))
        if times_value <= final_result:
            fringe.append((current_id + 1, times_value))
        if extended and concat_value <= final_result:
            fringe.append((current_id + 1, concat_value))
    # Everything has been pruned
    return 0

total_sum = sum(dfs_calibration(calib) for calib in all_calibrations)
print("The total calibration result is", total_sum)

total_sum = sum(dfs_calibration(calib, extended=True) for calib in all_calibrations)
print("The total calibration extended result is", total_sum)
