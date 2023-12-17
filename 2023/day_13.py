"""This is day 13 of advent of code 2023"""
import numpy as np
from utils.file import list_lines

with open(file="inputs/day_13.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

def count_differences(a: list[list[str]], b:list[list[str]]) -> int:
    """Count difference between two list with same shape"""
    n_rows = len(a)
    n_cols = len(a[0])
    count =0
    for i in range(n_rows):
        for j in range(n_cols):
            if a[i][j] != b[i][j]:
                count +=1
    return count

class Land:
    """A class to define a land"""

    def __init__(self, lines) -> None:
        self.space = [[*line] for line in lines]
        self.n_rows = len(self.space)
        self.n_cols = len(self.space[0])

    def nb_sym_rows(self):
        """Compute the number (index) of the different rows symetries"""
        number_sym_rows = []
        for i in range(1, len(self.space)):
            # Create the new rows by symmetry
            new_rows = []
            mask = self.space[:i]
            new_rows.extend(mask)
            while len(new_rows) < len(self.space):
                new_rows.extend(mask[::-1])
                new_rows.extend(mask)
            new_rows = new_rows[:len(self.space)]
            if count_differences(new_rows, self.space) == 1:
            #if new_rows == self.space:
                number_sym_rows.append(i)

        # Backwards
        for i in range(1, len(self.space)):
            # Create the new rows by symmetry
            new_rows = []
            temp_rows = []
            mask = self.space[i:]
            new_rows.extend(mask)
            while len(new_rows) < len(self.space):
                temp_rows.clear()
                temp_rows.extend(mask)
                temp_rows.extend(mask[::-1])
                temp_rows.extend(new_rows)
                new_rows = temp_rows.copy()
            new_rows = new_rows[-len(self.space):]
            if count_differences(new_rows, self.space) == 1:
            #if new_rows == self.space:
                number_sym_rows.append(i)
        if len(number_sym_rows) != 0:
            return [min(number_sym_rows)]
        return number_sym_rows

    def nb_sym_cols(self):
        """Compute the number (index) of the different cols symetries"""
        number_sym_cols = []
        current_space_np = np.asarray(self.space)
        current_space_np = np.transpose(current_space_np)
        current_space: list = current_space_np.tolist()
        for i in range(1, len(current_space)):
            # Create the new cols by symmetry
            new_cols = []
            mask = current_space[:i]
            new_cols.extend(mask)
            while len(new_cols) < len(self.space[0]):
                new_cols.extend(mask[::-1])
                new_cols.extend(mask)
            new_cols = new_cols[:len(self.space[0])]
            if count_differences(new_cols, current_space) == 1:
            #if new_cols == current_space:
                number_sym_cols.append(i)

        # Backwards
        for i in range(1, len(current_space)):
            # Create the new cols by symmetry
            new_cols = []
            temp_cols = []
            mask = current_space[i:]
            new_cols.extend(mask)
            while len(new_cols) < len(self.space[0]):
                temp_cols.clear()
                temp_cols.extend(mask)
                temp_cols.extend(mask[::-1])
                temp_cols.extend(new_cols)
                new_cols = temp_cols.copy()
            new_cols = new_cols[-len(self.space[0]):]
            if count_differences(new_cols, current_space) == 1:
            #if new_cols == current_space:
                number_sym_cols.append(i)
        if len(number_sym_cols) != 0:
            return [min(number_sym_cols)]
        return number_sym_cols



all_lands: list[Land] = []
current_seq = []
for current_line in all_lines:
    if current_line == '' and len(current_seq) != 0:
        all_lands.append(Land(current_seq))
        current_seq = []
    else:
        current_seq.append(current_line)
if len(current_seq) != 0:
    all_lands.append(Land(current_seq))

nb_sym_row = [sum(land.nb_sym_rows()) for land in all_lands]
nb_sym_col = [sum(land.nb_sym_cols()) for land in all_lands]

print(f"The expected number is : {sum(nb_sym_col) + 100 * sum(nb_sym_row)}")
