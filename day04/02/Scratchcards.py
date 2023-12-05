import os


def getInput(pathFile):
    total_sum = 0
    result_array = []
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
                found_count += 1
        nb = 1
        temp = []
        while nb <= found_count:
            nbb = 1
            while nbb <= int(line[0]):
                temp.append(nb + int(line[0]))
                nbb += 1
            nb += 1
        result_array.extend(temp)
        print(result_array)
        total_sum += power 
    return total_sum

# Example usage
print(getInput("Scratchcards.txt"))




                