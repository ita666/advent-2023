import os


def getInput(pathFile):
    total_sum = 0
    with open(pathFile, "r") as file:
        lines = file.readlines()
    split_lines = [line.split(':') for line in lines]
    split_lines = [[part.replace("Card ", "") for part in line] for line in split_lines]
    for line in split_lines:
        array = line[1].split("|")
        game = array[0].split()
        values = array[1].split()

        power = 1
        found_count = 0
        for number in game:
            if any(element in game for element in values) == False:
                power = 0
                break
            if number in values:
                if found_count > 0: 
                    power *= 2
                found_count += 1 
        total_sum += power 
    return total_sum

# Example usage
print(getInput("Scratchcards.txt"))




                