"""This file contains utils functions to format a file"""
from io import TextIOWrapper
from typing import List
from itertools import islice

def list_lines(f: TextIOWrapper) -> List[str]:
    """
    Convert a file into a list where each line is an item of the list
    """
    lines: List[str] = f.readlines()
    lines = list(map(lambda x: x[:-1], lines))
    return lines

def list_lines_not_empty(f: TextIOWrapper) -> List[str]:
    """
    Convert a file into a list where each line not empty is an item of the list
    """
    lines: List[str] = f.readlines()
    lines = list(map(lambda x: x[:-1],filter(lambda x: x != '', lines)))
    return lines

def list_specific_lines(f: TextIOWrapper, min_value:int, max_value:int) -> List[str]:
    """
    Convert some lines of the file into a list 
    """
    return [line[:-2] for line in islice(f, min_value-1, max_value)]
