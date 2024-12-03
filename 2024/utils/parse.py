"""A file with all the scripts dedicated to parsing"""
from pathlib import Path

def simple_parse(f: Path):
    """Parse and return a list of strings"""
    with open(f, mode='r', encoding='utf-8') as file:
        all_lines = file.readlines()
    # remove \n split 
    return list(map(lambda x: x[:-1], all_lines))

def simple_read(f: Path):
    """Return all the lines"""
    with open(f, mode='r', encoding='utf-8') as file:
        all_lines = file.read()
    return all_lines

def parse_number(f: Path):
    """Parse and return a list of list of number"""
    with open(f, mode='r', encoding='utf-8') as file:
        all_lines = file.readlines()
    # remove \n split and convert to number
    return [[int(y) for y in x[:-1].split(" ")] for x in all_lines]
