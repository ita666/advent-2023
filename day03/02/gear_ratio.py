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
    if char.isdigit():
        return True
    else:
        return False
def find_complete_number(array, x, initial_y):
    # Scan left from the initial position
    left_number_str = ''
    y = initial_y
    while y >= 0 and array[x][y].isdigit():
        left_number_str = array[x][y] + left_number_str
        y -= 1
    # Scan right from the position next to the initial position
    right_number_str = ''
    y = initial_y + 1
    while y < len(array[0]) and array[x][y].isdigit():
        right_number_str += array[x][y]
        y += 1
    # Combine the two parts
    complete_number_str = left_number_str + right_number_str
    return int(complete_number_str) if complete_number_str else None
	
def check_eight_directions(array):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(len(array)):
        j = 0
        while j < len(array[i]):
            if array[i][j] == '*':
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if 0 <= x < len(array) and 0 <= y < len(array[0]) and valid_adj_char(array[x][y]):
                        print(array[x][y])
                        print(find_complete_number(array, x, y))
                        print()
            j += 1

        
array = makeDoubleArray("gear_ratio.txt")
#printDoubleArray(array)
print(check_eight_directions(array))
