"""Day 11 AoC 2024"""
from collections import Counter
from dataclasses import dataclass
from copy import deepcopy
from utils.parse import simple_parse

line = simple_parse("inputs/11.txt")
line = line[0].split(" ")
int_line = [int(elt) for elt in line]

@dataclass
class Stone:
    """A dataclass to represent stones"""
    value: int
    amount: int

    def update(self):
        """Blink the stone"""
        if self.value == 0:
            self.value = 1
            return [self]
        str_value = str(self.value)
        n_str = len(str_value)
        if n_str % 2 == 0:
            return [Stone(int(str_value[:int(n_str / 2)]), self.amount),
                    Stone(int(str_value[int(n_str / 2):]), self.amount)]
        self.value *= 2024
        return [self]


def blink(stones, n_blink):
    """Compute the number of stones after n blinks"""
    for _ in range(n_blink):
        tmp_blink = [new_stones for stone in stones for new_stones in stone.update()]
        counter_blink = Counter()
        for stone in tmp_blink:
            counter_blink.update({stone.value: stone.amount})
        stones = [Stone(value=value, amount=counter_blink[value]) for value in counter_blink]

    n_stones = sum(stone.amount for stone in stones)
    print(f"The number of stones after {n_blink} blinks is", n_stones)
    return n_stones


# Create stones
list_stones = [Stone(value, 1) for value in int_line]
# Part 1
blink(deepcopy(list_stones), 25)

# Part 2
blink(deepcopy(list_stones), 75)
