
def start_marker(text):
    index = 4
    mySet = set(text[:4])
    while (len(mySet) != 4):
        index += 1
        mySet = set(text[index-4:index])
    return index


def message_marker(text):
    index = 14
    mySet = set(text[:14])
    while (len(mySet) != 14):
        index += 1
        mySet = set(text[index-14:index])
    return index


with open('inputs/6.txt', 'r') as file:
    data = file.read().replace('\n', '')
    first_start_marker = start_marker(data)
    first_message_marker = message_marker(data)


print(f"The first marker is at index {first_start_marker}")
print(f"The first message marker is at index {first_message_marker}")
