"""Day 1 AoC 2024"""
from collections import Counter
import numpy as np

with open("inputs/1.txt", mode='r', encoding='utf-8') as f:
    all_lines = f.readlines()

all_lines = list(map(lambda line: line[:-1].split(' '*3), all_lines))

first_column = np.array([line[0] for line in all_lines], dtype=int)
second_column = np.array([line[1] for line in all_lines], dtype=int)

def part_1(first, second):
    """Compute the distance between two lists"""
    first.sort()
    second.sort()

    difference = np.abs(second - first)

    return difference.sum()
print("The total distance is", part_1(first_column, second_column))

def part_2(first, second):
    """Compute the similarity score between the two lists"""
    count_second_list = Counter(second)

    similarity_score = 0
    for first_value in first:
        if first_value in count_second_list:
            similarity_score += first_value * count_second_list[first_value]
    
    return similarity_score

print("The similarity score is", part_2(first_column, second_column))
