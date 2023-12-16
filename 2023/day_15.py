"""This is day 15 of advent of code 2023"""

with open(file="inputs/day_15.txt", mode='r', encoding="utf-8") as f:
    all_lines = f.readline()[:-1]


def translate(character: str, current_value: int):
    """Translate a character according to the hash algorithm"""
    return (current_value + ord(character)) * 17 % 256


def translate_word(word: str):
    """Translate a word according to the hash algorithm"""
    current_value = 0
    for character in word:
        current_value = translate(character, current_value)
    return current_value


def part_1(line: str):
    """Return the list of current values"""
    all_curr_values = []
    steps = line.split(',')
    for step in steps:
        all_curr_values.append(translate_word(step))
    return all_curr_values


def create_boxes(line: str):
    """ Generate all the boxes """
    steps = line.split(",")
    all_boxes = [[] for _ in range(256)]
    for step in steps:
        if '=' in step:
            lens, focal = step.split('=')
            box_idx = translate_word(lens)
            for ind, curr_lens in enumerate(all_boxes[box_idx]):
                if curr_lens[0] == lens:
                    # Check if already exists
                    all_boxes[box_idx][ind][1] = int(focal)
                    break
            else:
                all_boxes[box_idx].append([lens, int(focal)])
        else:
            lens = step[:-1]
            box_idx = translate_word(lens)
            for ind, curr_lens in enumerate(all_boxes[box_idx]):
                if curr_lens[0] == lens:
                    # Check if already exists
                    del all_boxes[box_idx][ind]
                    break
    return all_boxes

def part_2(line):
    """Print the solution of part 2"""
    boxes = create_boxes(line)
    total_focusing_power = 0
    for i, box in enumerate(boxes):
        for j, elt in enumerate(box):
            total_focusing_power += (i + 1) * (j + 1) * elt[1]

    print(f"The total focusing power is {total_focusing_power}")

#Run part 1
all_current_values = part_1(all_lines)
print(f"The sum of all current values is {sum(all_current_values)}")

#Run part 2
part_2(all_lines)
