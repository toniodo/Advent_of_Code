
points = {
    "Lose": 0,
    "Draw": 3,
    "Win": 6,
    'A': 1,
    'B': 2,
    'C': 3,
    'X': "Lose",
    'Y': "Draw",
    'Z': "Win"
}


def PapSciRoc(a, b):
    if (b > 68):
        b -= 23
    totalPoints = 0
    if (a == b):
        totalPoints += points["Draw"]
    elif (a < b):
        if (b-a == 1):
            totalPoints += points["Win"]
    elif (a > b):
        if (a-b != 1):
            totalPoints += points["Win"]
    totalPoints += points[chr(b)]
    return totalPoints


def win(a):
    if (a == 'A'):
        return 'B'
    elif (a == 'B'):
        return 'C'
    else:
        return 'A'


def draw(a):
    return a


def lose(a):
    if (a == 'A'):
        return 'C'
    elif (a == 'B'):
        return 'A'
    else:
        return 'B'


def calculatePoints(result, ennemy):
    player = ''
    resultChar = points[result]
    if (resultChar == "Win"):
        player = win(ennemy)
    elif (resultChar == "Draw"):
        player = draw(ennemy)
    else:
        player = lose(ennemy)
    return PapSciRoc(ord(ennemy), ord(player))


input = open("inputs/2.txt", 'r')

globalPoint = 0
pointPart2 = 0
list = input.readlines()
for i in list:

    globalPoint += PapSciRoc(ord(i[0]), ord(i[2]))
    pointPart2 += calculatePoints(i[2], i[0])

print(f"The total points are {globalPoint}\n")
print(f"Points for part 2 are {pointPart2}\n")
