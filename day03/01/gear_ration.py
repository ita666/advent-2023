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

def checkchar(array)
	#Check arround number if . or number
	strnum
	for i in range(1,len(array)-1):
		for j in range(1,len(array[i])-1):
			if array[i][j].isdigit():
				append(strnum,array[i][j])
				if !array[i-1][j].isdigit() and array[i-1][j] != '.':
					while array[i-1][j].isdigit():
						append(strnum,array[i-1][j])
					return int(strnum)



def checkchar(array):
    # Function to check around a number if it's a digit or a dot in all directions
    def get_number_at(i, j, di, dj):
        # Collects a number starting at (i, j) and going in the direction (di, dj)
        strnum = ''
        while 0 <= i < len(array) and 0 <= j < len(array[i]) and (array[i][j].isdigit() or array[i][j] == '.'):
            strnum += array[i][j]
            i += di
            j += dj
        return strnum

    # Directions vectors (up, down, left, right, diagonals)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    numbers = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j].isdigit():
                # Check the cell directly above
                if i == 0 or (not array[i-1][j].isdigit() and array[i-1][j] != '.'):
                    for di, dj in directions:
                        num = get_number_at(i + di, j + dj, di, dj)
                        if num:
                            numbers.append(num)

    return numbers

# Test the function with your array
array = [
    ['.', '.', '.', '.'],
    ['.', '4', '.'],
    ['.', '.', '.', '.']
]

print(checkchar(array))

array = makeDoubleArray("gear_ratio.txt")
for line in array:
	print(line)

