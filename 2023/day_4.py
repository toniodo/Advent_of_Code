"""This is day 4 of Advent of Code 2023"""
from typing import List
from utils.file import list_lines


def part_1(lines: List[List[List[int]]]):
    """Prints the solution of part 1"""
    sum_points = 0
    for games in lines:
        winning_numbers = games[0]
        my_numbers = games[1]
        count = 0
        for number in my_numbers:
            if number in winning_numbers:
                count += 1
        # Update the sum of points
        if count != 0:
            sum_points += 2**(count - 1)

    print(f"The sum of all the points is {sum_points}")

def part_2(lines: List[List[List[int]]]):
    """Prints the solution of part 2"""
    max_card = len(lines)
    scratchcards = [1]*max_card
    for i, games in enumerate(lines):
        winning_numbers = games[0]
        my_numbers = games[1]
        count = 0
        for number in my_numbers:
            if number in winning_numbers:
                count += 1
        # Update the number of cards
        if count != 0:
            for j in range(1,count+1):
                if i+j <= max_card :
                    scratchcards[i+j] += scratchcards[i]

    print(f"The sum of all the won scratchcards is {sum(scratchcards)}")

with open("inputs/day_4.txt", 'r', encoding='utf-8') as f:
    all_lines = list_lines(f)

# all_lines[game id][type number][value id]
all_lines = map(lambda x: x.split(":")[1], all_lines)
all_lines = map(lambda x: x.split('|'), all_lines)
all_lines = [[g_i.split(' ') for g_i in game_id] for game_id in all_lines]
all_lines = [[filter(lambda x: x!= '', g_i) for g_i in game_id] for game_id in all_lines]
all_lines = [[list(map(int, g_i)) for g_i in game_id] for game_id in all_lines]

# Run part 1
part_1(all_lines)

# Run part 2
part_2(all_lines)
