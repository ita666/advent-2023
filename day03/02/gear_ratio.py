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
    for i in range(len(array)):
        j = 0
        while j < len(array[i]):
            if array[i][j] == '*':
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if 0 <= x < len(array) and 0 <= y < len(array[0]) and valid_adj_char(array[x][y]):
                        #print(x)
                       # print(y)
                        #print()
                        #check the direction if it is a number using a decrement for loop
                        for i in range(y, 0, -1 ):
                            if array[x][y - i] != '.':
                                print(f'test :{array[x][i]}')
                        print(array[x][y])
                        print()
                        #if array[x][y] == '0':
                print()
                
            j += 1
        
                

array = makedoubleArray("gear_ratio.txt")
#printDoubleArray(array)
print(check_eight_directions(array))
