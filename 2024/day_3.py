"""Day 3 AoC 2024"""
import re
from utils.parse import simple_read

def find_mod(lines:list[str]):
    """Find all patterns matching mul()"""
    global_sum = 0
    all_mod = re.findall(r"mul\(\d+,\d+\)", lines)
    # Only take the number and comma
    all_mod = list(map(lambda x: x[4:-1].split(","), all_mod))
    for n1, n2 in all_mod:
        global_sum += int(n1)*int(n2)
    print("The global sum is", global_sum)
    return global_sum

def find_mod_do_dont(lines:list[str]):
    """Find all patterns matching mul()"""
    all_mod = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", lines)
    # do() as a boolean value
    do = True
    global_sum = 0
    for value in all_mod:
        if value == "do()":
            do = True
        elif value == "don't()":
            do = False
        elif do:
            n1,n2 = value[4:-1].split(",")
            global_sum += int(n1)*int(n2)
    print("The global sum with do and don't is", global_sum)
    return global_sum



if __name__ =='__main__':
    all_lines = simple_read("inputs/3.txt")
    # Part 1
    find_mod(all_lines)
    # Part 2
    find_mod_do_dont(all_lines)
