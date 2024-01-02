"""This is day 19 of advent of code 2023"""
import re
import operator
from copy import deepcopy
from utils.file import list_lines

with open(file="inputs/day_19.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

class Workflow:
    """Class to represent a workflow"""
    comparaison= {'<': operator.lt, '>': operator.gt}

    def __init__(self, line: str):
        self.id, content = line.split('{')
        # Remove } from content
        content = content[:-1]
        # Split into lists [var, symbol, value, ':', destination]
        content = content.split(',')
        content = [re.split(r'(>|:|<)', comp) for comp in content]
        self.content = content

    def destination(self, x:int, m:int, a:int, s:int):
        """Return the label of the destination"""
        for var, symbol, value, _, dest in self.content[:-1]:
            if var == 'x' and self.comparaison[symbol](x, int(value)):
                return dest
            if var == 'm' and self.comparaison[symbol](m, int(value)):
                return dest
            if var == 'a' and self.comparaison[symbol](a, int(value)):
                return dest
            if var == 's' and self.comparaison[symbol](s, int(value)):
                return dest
        return self.content[-1][0]


def number_accepted(parts: list[list[int]], workflows):
    """Print the number of accepted parts"""
    count_a = 0
    for x,m,a,s in parts:
        # First workflow is named 'in'
        label = workflows['in'].destination(x,m,a,s)
        while label not in {'A','R'}:
            label = workflows[label].destination(x,m,a,s)
        if label == 'A':
            count_a += x+m+a+s
    print(f"The number of accepted part is : {count_a}")


sep_space = all_lines.index('')
#Create dict of workflow object with id as key
workflows: dict[str,Workflow] = {}
for line in all_lines[:sep_space]:
    obj = Workflow(line)
    workflows[obj.id] = obj

# Part 1
parts = [line[1:-1].split(',') for line in all_lines[sep_space+1:]]
#Keep only values for x, m, a and s
parts = [list(map(lambda x: int(x[2:]), part)) for part in parts]
number_accepted(parts, workflows)

# Part 2
#Create bounds for all values [x,m,a,s]
min_max_values = {'x':[1, 4000], 'm':[1, 4000], 'a':[1, 4000], 's':[1, 4000]}

def split_and_count(label, range_dict: dict[str,list[int]], workflows):
    """Split and return the total count"""
    if label == 'A':
        count = 1
        for min_val, max_val in range_dict.values():
            count *= (max_val-min_val +1)
        return count
    if label == 'R':
        return 0
    #Otherwise
    current_workflow = workflows[label]
    current_range = deepcopy(range_dict)
    count = 0
    for var, symbol, value, _, dest in current_workflow.content[:-1]:
        int_value = int(value)
        passed = False
        if symbol == '<':
            # If all the range is not include
            if not current_range[var][1] < int_value and current_range[var][0] < int_value:
                first_part = deepcopy(current_range)
                first_part[var][1] = int_value-1
                count += split_and_count(dest, first_part, workflows)
                current_range[var][0] = int_value
                continue
            # All the range is outside the condition
            if current_range[var][0] >= int_value:
                continue
        elif symbol == '>':
            if not current_range[var][0] > int_value and current_range[var][1] > int_value:
                second_part = deepcopy(current_range)
                second_part[var][0] = int_value+1
                count += split_and_count(dest, second_part, workflows)
                current_range[var][1] = int_value
                continue
            if current_range[var][1] <= int_value:
                continue
        count += split_and_count(dest, current_range, workflows)
        passed = True
    if not passed:
        count += split_and_count(current_workflow.content[-1][0], current_range, workflows)
    return count

total_score = split_and_count('in', min_max_values, workflows)
print(f"The final total score is : {total_score}")
