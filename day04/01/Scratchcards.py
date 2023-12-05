import os


def getInput(pathFile):
    total_sum = 0
    with open(pathFile, "r") as file:
        lines = file.readlines()

    for line in lines:
        array = line.split("|")
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




                