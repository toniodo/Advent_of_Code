def intersectionItem(liste):
    n = len(liste)
    list1 = liste[:(n//2)]
    list2 = liste[(n//2):]
    return intersection(list1, list2)


def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))


input = open("inputs/3.txt", 'r')
lines = input.readlines()


def calculatePrio(letter):
    if (letter.isupper()):
        return (ord(j) % 64) + 26
    else:
        return ord(j) % 96


sum = 0
for i in lines:
    character = intersectionItem(i)
    for j in character:
        sum += calculatePrio(j)

sum2 = 0
for i in range(0, len(lines), 3):
    firstInter = intersection(lines[i], lines[i+1])
    secondInter = intersection(firstInter, lines[i+2])
    for j in secondInter:
        if (j != '\n'):
            sum2 += calculatePrio(j)


print(f"Total value is : {sum}")

print(f"Total value with badges is : {sum2}")
