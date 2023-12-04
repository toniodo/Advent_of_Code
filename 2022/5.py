import re

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

stacks = {
    "1": stack1,
    "2": stack2,
    "3": stack3,
    "4": stack4,
    "5": stack5,
    "6": stack6,
    "7": stack7,
    "8": stack8,
    "9": stack9,
}

input = open("inputs/5.txt", 'r')
listFile = input.readlines()

# Fill stacks
for j in range(7, -1, -1):
    for i in range(1, 36, 4):
        stacks[str((i // 4)+1)].append(listFile[j][i])

# clean list
for j in range(1, 10):
    stacks[str(j)] = [ele for ele in stacks[str(j)] if ele.strip()]

# Part 1


def part1():
    for i in range(10, len(listFile)):
        # i[10] is the begin
        number = re.findall('[0-9]+', listFile[i])
        for j in range(int(number[0])):

            stacks[str(number[2])].append(stacks[str(number[1])][-1])
            # pop final element
            stacks[str(number[1])].pop()

    for i in range(1, 10):
        print(stacks[str(i)][-1])
    print("End of part 1")


# Part 2
for i in range(10, len(listFile)):
    # i[10] is the begin
    number = re.findall('[0-9]+', listFile[i])
    finalElt = stacks[str(number[1])][-int(number[0]):]

    stacks[str(number[2])].extend(finalElt)
    # pop final element
    stacks[str(number[1])] = stacks[str(number[1])][: -int(number[0])]

for i in range(1, 10):
    print(stacks[str(i)][-1], end="")
print("\nEnd of part 2")

input.close()
