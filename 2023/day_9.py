"""This is day 9 of advent of code 2023"""
from itertools import pairwise
from utils.file import list_lines

with open(file="inputs/day_9.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)

class Sequence:
    """This class represents a node of a sequence"""
    def __init__(self, list_values, parent = None) -> None:
        self.values = list_values
        self.parent = parent
        self.child: self

    @staticmethod
    def from_string(line_str: str):
        """Convert a line string into a Sequence"""
        return Sequence(list(map(int,line_str.split(' '))))

    def is_leaf(self):
        """Check if the current node is a leaf"""
        n_values = len(self.values)
        n_zeros = len(list(filter(lambda x: x==0, self.values)))
        return n_values == n_zeros

    def forward(self):
        """ From a root node """
        current_child = self
        while not current_child.is_leaf():
            values_child = []
            for a, b in pairwise(current_child.values):
                values_child.append(b-a)
            current_child.child = Sequence(values_child, current_child)
            current_child = current_child.child
        return current_child

    def backpropagate(self):
        """ From a child node """
        if self.is_leaf():
            current_seq = self
            while current_seq.parent is not None:
                parent = current_seq.parent
                parent.values.append(parent.values[-1] + current_seq.values[-1])
                current_seq = current_seq.parent
        else:
            print("Cannot backpropagate, not a leaf !")

    def extrapolate(self):
        """Return the last value estimated of the sequence"""
        return self.values[-1]

    def reverse_values(self):
        """Retrun the reversed list of values"""
        self.values = self.values[::-1]

all_sequences = set()
for line in all_lines:
    all_sequences.add(Sequence.from_string(line))

for seq in all_sequences:
    seq.forward().backpropagate()

sum_extrapolation = 0
for seq in all_sequences:
    sum_extrapolation += seq.extrapolate()

print(f"The sum of right extrapolation is {sum_extrapolation}")

# Part 2
all_sequences = set()
for line in all_lines:
    all_sequences.add(Sequence.from_string(line))

for seq in all_sequences:
    seq.reverse_values()
    seq.forward().backpropagate()

sum_extrapolation = 0
for seq in all_sequences:
    sum_extrapolation += seq.extrapolate()

print(f"The sum of left extrapolation is {sum_extrapolation}")
