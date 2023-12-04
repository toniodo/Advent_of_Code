input = open("inputs/4.txt", 'r')
file = input.readlines()


def inclusion(value):
    (infA, supA, infB, supB) = value

    if (infA <= infB and supA >= supB):
        return 1
    elif (infB <= infA and supB >= supA):
        return 1
    else:
        return 0


def overlap(value):
    (infA, supA, infB, supB) = value
    return (infA <= supB and infA >= infB) or (infB <= supA and infB >= infA)


def values(line):
    number1 = 0
    number2 = 0
    number3 = 0
    number4 = 0
    hiffen = 0
    coma = 0
    i = 0
    while (line[i] != '-'):
        i += 1
    hiffen = i
    number1 = int(line[:hiffen])
    while (line[i] != ','):
        i += 1
    coma = i
    number2 = int(line[(hiffen+1):coma])
    while (line[i] != '-'):
        i += 1
    hiffen = i
    number3 = int(line[(coma+1):hiffen])
    while (line[i] != '\n'):
        i += 1
    number4 = int(line[(hiffen+1):i])
    return number1, number2, number3, number4


nbInclusion = 0
for i in file:
    nbInclusion += inclusion(values(i))

print(f"There are {nbInclusion} inclusions")

overlaps = 0
for j in file:
    overlaps += overlap(values(j))

print(f"There are {overlaps} overlaps in total")
