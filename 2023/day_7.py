"""This is day 7 of advent of code 2023"""
from collections import Counter
from utils.file import list_lines

with open(file="inputs/day_7.txt", mode='r', encoding="utf-8") as f:
    all_lines = list_lines(f)


class Hand:
    """A class to represent a hand"""

    def __init__(self, hand_line):
        self.cards = [*hand_line[:5]]
        self.points = int(hand_line[6:])
        self.priority_order = {
            '2': 0,
            '3': 1,
            '4': 2,
            '5': 3,
            '6': 4,
            '7': 5,
            '8': 6,
            '9': 7,
            'T': 8,
            'J': 9,
            'Q': 10,
            'K': 11,
            'A': 12}
        occurences = Counter(self.cards).values()
        max_occurences = max(occurences)
        if max_occurences >= 4:
            self.type_hand = max_occurences + 1
        elif max_occurences == 3:
            # Full house
            if min(occurences) == 2:
                self.type_hand = 4
            else:
                # Three in a kind
                self.type_hand = 3
        elif max_occurences == 2:
            count_occurences = Counter(occurences).values()
            # Two pairs
            if max(count_occurences) == 2:
                self.type_hand = 2
            else:
                # One pair
                self.type_hand = 1
        else:
            self.type_hand = 0

    def __gt__(self, other):
        """ Returns True if self is greater than other"""
        if self.type_hand > other.type_hand:
            return True
        if self.type_hand < other.type_hand:
            return False
        for i, j in zip(self.cards, other.cards):
            order_i = self.priority_order[i]
            order_j = self.priority_order[j]
            if order_i > order_j:
                return True
            if order_i < order_j:
                return False
        return None


class HandJoker(Hand):
    """A class to represent a hand"""

    def __init__(self, hand_line):
        self.cards = [*hand_line[:5]]
        self.points = int(hand_line[6:])
        self.priority_order = {
            'J': 0,
            '2': 1,
            '3': 2,
            '4': 3,
            '5': 4,
            '6': 5,
            '7': 6,
            '8': 7,
            '9': 8,
            'T': 9,
            'Q': 10,
            'K': 11,
            'A': 12}
        counter_cards = Counter(self.cards)
        nb_J = counter_cards["J"]
        if nb_J == 0:
            # Same as part 1
            occurences = counter_cards.values()
            max_occurences = max(occurences)
            if max_occurences >= 4:
                self.type_hand = max_occurences + 1
            elif max_occurences == 3:
                # Full house
                if min(occurences) == 2:
                    self.type_hand = 4
                else:
                    # Three in a kind
                    self.type_hand = 3
            elif max_occurences == 2:
                count_occurences = Counter(occurences)[2]
                # Two pairs
                if count_occurences == 2:
                    self.type_hand = 2
                else:
                    # One pair
                    self.type_hand = 1
            else:
                self.type_hand = 0
        # In case there is a J
        else:
            card_without_j = []
            for card in self.cards:
                if card != 'J':
                    card_without_j.append(card)
            if len(card_without_j) != 0:
                # Same as part 1
                occurences = Counter(card_without_j).values()
                max_occurences = max(occurences)
                if max_occurences == 4:
                    self.type_hand = max_occurences + 1
                elif max_occurences == 3:
                    # Three in a kind
                    self.type_hand = 3
                elif max_occurences == 2:
                    count_occurences = Counter(occurences)[2]
                    # Two pairs
                    if nb_J < 2 and count_occurences == 2:
                        self.type_hand = 2
                    else:
                        # One pair
                        self.type_hand = 1
                else:
                    self.type_hand = 0

                if nb_J == 1:
                    if self.type_hand in {1, 2, 3}:
                        self.type_hand += 2
                    else:
                        self.type_hand += 1
                elif nb_J == 2:
                    if self.type_hand in {0, 3}:
                        self.type_hand += 3
                    else:
                        self.type_hand += 4
                elif nb_J == 3:
                    self.type_hand += 5
                elif nb_J == 4:
                    self.type_hand = 6
            else:
                self.type_hand = 6


def part_1(lines):
    """Prints part 1"""
    all_hands = []
    for hand in lines:
        all_hands.append(Hand(hand))
    all_hands.sort()

    total_score = 0
    for ind, hand in enumerate(all_hands):
        total_score += (ind + 1) * hand.points

    print(f"Le score total est de : {total_score}")


def part_2(lines):
    """Prints part 2"""
    all_hands = []
    for hand in lines:
        all_hands.append(HandJoker(hand))
    all_hands.sort()

    total_score = 0
    for ind, hand in enumerate(all_hands):
        total_score += (ind + 1) * hand.points

    print(f"Le score total est de : {total_score}")

# Run part 1
part_1(all_lines)

# Run part 2
part_2(all_lines)
