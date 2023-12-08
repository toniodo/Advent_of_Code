"""This is day 8 of advent of code 2023"""
from math import lcm
from itertools import cycle
from utils.file import list_lines

with open(file="inputs/day_8.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

seq = [*all_lines[0]]
intersect = {line[0:3]: (line[7:10], line[12:15]) for line in all_lines[2:]}

def part_1(seq_actions, intersections):
    """ Prints the answer of part 1"""
    steps = 0
    iter_action = cycle(seq_actions)
    current_state = 'AAA'
    while current_state != 'ZZZ':
        action = next(iter_action)
        if action == 'L':
            current_state = intersections[current_state][0]
        else:
            current_state = intersections[current_state][1]
        steps+=1

    print(f"Le nombre total de step est de {steps}")

def part_2(seq_actions, intersections):
    """ Prints the answer of part 2"""
    all_current_states = list(filter(lambda x: x[-1] == 'A', intersections.keys()))
    all_states_steps = [0]*len(all_current_states)
    for idx, state in enumerate(all_current_states):
        steps = 0
        current_state = state
        iter_action = cycle(seq_actions)
        while current_state[-1] != 'Z':
            action = next(iter_action)
            if action == 'L':
                current_state = intersections[current_state][0]
            else:
                current_state = intersections[current_state][1]
            steps+=1
        all_states_steps[idx] = steps

    print(f"Le nombre total de step est de {lcm(*all_states_steps)}")

# Part 1
part_1(seq, intersect)

# Part 2
part_2(seq, intersect)
