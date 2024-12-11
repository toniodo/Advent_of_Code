"""Day 5 AoC 2024"""
from itertools import combinations

with open("inputs/5.txt", mode='r', encoding='utf-8') as f:
    all_lines = f.readlines()

# Parsing
all_lines = list(map(lambda x: x[:-1], all_lines))
separation_index = all_lines.index("")

rules_list = all_lines[:separation_index]
rules_list = list(map(lambda x: x.split('|'), rules_list))
updates_pages = all_lines[separation_index + 1:]
updates_pages = list(map(lambda x: x.split(','), updates_pages))
updates_pages = [[int(update) for update in updates] for updates in updates_pages]

set_rules = {(int(rule[0]), int(rule[1])) for rule in rules_list}


def check_update(update: list[list[int]], rules: set[tuple[int, int]]) -> bool:
    all_pairs = set(combinations(update[::-1], 2))
    intersection = rules.intersection(all_pairs)
    if len(intersection) != 0:
        return False
    return True


def valid_updates(all_updates: list[list[int]], rules: set[tuple[int, int]]) -> list[list[int]]:
    return [update for update in all_updates if check_update(update, rules)]


all_valid_updates = valid_updates(updates_pages, set_rules)

# Take the middle value of each valid update
sum_middle = sum(valid[int((len(valid) - 1) / 2)]for valid in all_valid_updates)
print("The sum of the middle of valid updates is", sum_middle)


def check_wrong_update(update: list[list[int]], rules: set[tuple[int, int]]) -> bool:
    all_pairs = set(combinations(update[::-1], 2))
    intersection = rules.intersection(all_pairs)
    if len(intersection) != 0:
        return True, intersection
    return False, set()


def wrong_updates(all_updates: list[list[int]], rules: set[tuple[int, int]]) -> list[list[int]]:
    corrected_updates = []
    for update in all_updates:
        wrong, intersection = check_wrong_update(update, rules)
        if wrong:
            # While it is a wrong update, we apply a rule
            while check_wrong_update(update, rules)[0]:
                wrong, intersection = check_wrong_update(update, rules)
                n1, n2 = intersection.pop()
                pos_n1 = update.index(n1)
                pos_n2 = update.index(n2)
                # Change position
                update[pos_n1] = n2
                update[pos_n2] = n1
            corrected_updates.append(update)
    return corrected_updates


all_wrong_updates = wrong_updates(updates_pages, set_rules)

# Take the middle value of each wrong update
sum_middle = sum(wrong[int((len(wrong) - 1) / 2)] for wrong in all_wrong_updates)
print("The sum of the middle of wrong updates is", sum_middle)
