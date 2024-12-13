"""Day 13 AoC 2024"""
from dataclasses import dataclass
import re
from utils.parse import simple_parse


@dataclass
class Game:
    """A Class to represent the claw problem"""
    x_move: list[int,int]
    y_move: list[int,int]
    goal: list[int,int]
    tok_x: int
    tok_y: int

    @property
    def min_token(self):
        """Compute the minimum tokens"""
        denominator = self.y_move[1]*self.x_move[0] - self.x_move[1]*self.y_move[0]
        if denominator == 0:
            # No solution
            return 0
        numerator_B = self.x_move[0] * self.goal[1] - self.x_move[1] * self.goal[0]
        numerator_A = self.y_move[1] * self.goal[0] - self.y_move[0] * self.goal[1]
        if not((numerator_B/denominator).is_integer() and (numerator_A/denominator).is_integer()):
            return 0
        button_B = numerator_B//denominator
        button_A = numerator_A//denominator

        return 3*button_A + button_B


all_lines= simple_parse("inputs/13.txt")

all_games = []
for n_game in range(0, len(all_lines)//4 +1):
    move_A = re.findall(r"\d+", all_lines[4*n_game])
    move_A = list(map(int, move_A))
    move_B = re.findall(r"\d+", all_lines[4*n_game + 1])
    move_B = list(map(int, move_B))
    prize = re.findall(r"\d+", all_lines[4*n_game + 2])
    prize = list(map(int, prize))

    all_games.append(Game(move_A, move_B, prize, 3, 1))

print("The total minimum token is", sum(game.min_token for game in all_games))

added_price = 1e13
for game in all_games:
    game.goal[0] += added_price
    game.goal[1] += added_price

print("The new total minimum token is", sum(game.min_token for game in all_games))

