import os

def makeDoubleArray(pathFile):
    # Read the file
    with open(pathFile, "r") as file:
        lines = file.readlines()
    if not lines:
        return []
    # Determine the number of columns based on the first line
    columns = len(lines[0].strip()) + 2 # Assuming each line ends with a newline character
    # Initialize the array
    array = [['.' for _ in range(columns)] for _ in range(len(lines) + 2)]
    # Fill the array
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            array[i + 1][j + 1] = char
    return array

def printDoubleArray(doubleArray):
    for i in range(len(doubleArray)):
        for j in range(len(doubleArray[0])):
            print(doubleArray[i][j], end='')
        print()

def valid_adj_char(char):
    if char != '.' and not char.isdigit():
        return True
    else:
        return False

def check_eight_directions(array):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    i = 0
    sum = 0
    for i in range(len(array)):
        num = []
        j = 0
        while j < len(array[i]):
            if array[i][j].isdigit():
                num.append(array[i][j])
                valid = False
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if 0 <= x < len(array) and 0 <= y < len(array[0]) and valid_adj_char(array[x][y]):
                        valid = True
                        break

                if valid:
                    k = 1
                    while j + k < len(array[i]) and array[i][j + k].isdigit():
                        num.append(array[i][j + k])
                        k += 1
                    j+= k
                    print(num)
                    sum +=int(''.join(num))
                    num = []
                j += 1
            else:
                num = []
                j += 1 
    return sum
        
                

array = makeDoubleArray("gear_ratio.txt")
#printDoubleArray(array)
print(check_eight_directions(array))
