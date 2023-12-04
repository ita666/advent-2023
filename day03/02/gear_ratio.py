import os

def makedoubleArray(pathFile):
    # Check if the file exists
    if not os.path.exists(pathFile):
        print(f"File does not exist: {pathFile}")
        return None
    lines = 2
    max_columns = 2
    file = open("gear_ratio.txt", 'r')
    for line in file:
        lines += 1
    max_columns += len(line.strip())
    doubleArray = [['.' for _ in range(max_columns)] for _ in range(lines)]

    # Fill the double array
    with open(pathFile, 'r') as file:
        for i in range(1, lines - 1):  # Exclude the extra lines
            line = file.readline().strip()
            for j in range(1, max_columns - 1):  # Exclude the extra columns
                doubleArray[i][j] = line[j - 1]

    return doubleArray

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

def check_eight_directions(array):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    i = 0
    sum = 0
    while i < len(array):
        num = []
        j = 0
        while j < len(array[i]):
            if array[i][j] == '*':
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
                j += 1  # Increment j even if not a digit is found
        i += 1
    return sum
        
                

array = makedoubleArray("gear_ratio.txt")
#printDoubleArray(array)
print(check_eight_directions(array))
