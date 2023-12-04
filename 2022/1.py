# A list to sum the total for each elf
totalByElf = []
# We open the input file in read mode
input = open("inputs/1.txt", 'r')
# We create a loop for each line
sum = 0
lines = input.readlines()
for currentLine in lines:
    # We read each line
    # If there is a blank space, we append the value in the list, and initialize the sum
    if (currentLine == '\n'):
        totalByElf.append(sum)
        sum = 0
    else:
        sum += int(currentLine)

# Part 1
# Using max function to find the maximum in the list
maxCalories = max(totalByElf)

# Print the result
print(f'The elf that posesses the maximum calories is : {maxCalories}\n')

# Part 2
# Collect the calories of the top Three Elves.
firstMax = max(totalByElf)
totalByElf.pop(totalByElf.index(max(totalByElf)))

secondMax = max(totalByElf)
totalByElf.pop(totalByElf.index(max(totalByElf)))

thirdMax = max(totalByElf)
totalByElf.pop(totalByElf.index(max(totalByElf)))

# Calculate the total
totalTopThree = firstMax + secondMax + thirdMax
# Print the result
print(f'The total calories of the top three Elves are : {totalTopThree}\n')
