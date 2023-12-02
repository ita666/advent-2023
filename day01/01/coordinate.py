import os

def get_coordinates_from_file(file_path):

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return 0

    result = 0

    with open(file_path, 'r') as file:
        for input_string in file:
            first_digit = None
            last_digit = None
            # Find the first digit
            for character in input_string:
                if character.isdigit():
                    first_digit = int(character)
                    break
            # Find the last digit
            for character in reversed(input_string.strip()):
                if character.isdigit():
                    last_digit = int(character)
                    break
            # Add calculated value
            if first_digit is not None and last_digit is not None:
                result += (first_digit * 10 + last_digit)
    return result

file_path = 'test.txt'
total_coordinates = get_coordinates_from_file(file_path)
print(total_coordinates)
