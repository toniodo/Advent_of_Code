"""This file contains utils functions to compute distances"""
from math import sqrt
from typing import Tuple


def euclidian_distance(a: Tuple[float | int, float | int],
                       b: Tuple[float | int, float | int]) -> float:
    """Compute the euclidian distance"""
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Compute the manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
