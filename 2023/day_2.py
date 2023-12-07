""" This is day 2 of Advent of Code 2023 """
from typing import List
from utils.file import list_lines


class GameSet:
    """A class to represent a set of a game"""

    def __init__(self, game: str):
        self.red: int = 0
        self.green: int = 0
        self.blue: int = 0

        # Separate the game of the sets
        game_and_set = game.split(':')
        self.game = int(game_and_set[0][5:])

        # Separate the sets
        str_sets: List[str] = game_and_set[1].split(';')
        for set_game in str_sets:
            # Spearate the colors of one set
            colors: List[str] = set_game.split(',')
            for color in colors:
                number_and_color: List[str] = color.split(' ')
                number_and_color = list(filter(lambda x: x != '', number_and_color))
                number = int(number_and_color[0])
                if number_and_color[1] == 'red' and number > self.red:
                    self.red = number
                elif number_and_color[1] == 'green' and number > self.green:
                    self.green = number
                elif number_and_color[1] == 'blue' and number > self.blue:
                    self.blue = number

    @property
    def power(self) -> int:
        """Return the power of a game"""
        return self.red * self.blue * self.green


class GameColor:
    """A class to represent a game"""

    def __init__(self, game_sets: List[GameSet], red: int, green: int, blue: int):
        self.max_red: int = red
        self.max_green: int = green
        self.max_blue: int = blue
        self.game_sets: List[GameSet] = game_sets

    def check(self, game_set: GameSet) -> bool:
        """Check if a set verifiy the condition"""
        return (
            game_set.red <= self.max_red and
            game_set.green <= self.max_green and
            game_set.blue <= self.max_blue
        )

    @property
    def power(self) -> int:
        """Sum the power of all games"""
        sum_power: int = 0
        for set_game in self.game_sets:
            sum_power += set_game.power
        return sum_power

    @property
    def sum_games(self) -> int:
        """Sum all the games that respect the criterion"""
        sum_valid: int = 0
        for set_game in self.game_sets:
            if self.check(set_game):
                sum_valid += set_game.game
        return sum_valid


with open("inputs/day_2.txt", 'r', encoding="utf-8") as f:
    l = list_lines(f)


def part_1(lines: List[str]) -> None:
    """Solves part 1"""
    all_game_set: List[GameSet] = [GameSet(line) for line in lines]
    current_game = GameColor(all_game_set, 12, 13, 14)
    print(f"The total sum of all the games is : {current_game.sum_games}")


def part_2(lines: List[str]) -> None:
    """Solves part 2"""
    all_game_set: List[GameSet] = [GameSet(line) for line in lines]
    current_game = GameColor(all_game_set, 12, 13, 14)
    print(f"The total sum of powers of all the games is : {current_game.power}")


# Run part 1
part_1(l) #2593

# Run part 2
part_2(l) #54699
