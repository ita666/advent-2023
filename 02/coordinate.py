import os


def convert_string(input_string):
    number_map = {
        "eight": '8', "seven": '7', "three": '3', "four": '4', 
        "five": '5', "nine": '9', "six": '6', "two": '2', 
        "one": '1', "ten": "10"
    }
    #check for long string first to be sure to avoid partial conversion
    for key in sorted(number_map.keys(), key=len, reverse=True):
        input_string = input_string.replace(key, number_map[key])
    
    return input_string

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
            #Convert the string to work with
            converted_string = convert_string(input_string)
            # Find the first digit
            for character in converted_string:
                if character.isdigit():
                    first_digit = int(character)
                    break
            # Find the last digit
            for character in reversed(converted_string.strip()):
                if character.isdigit():
                    last_digit = int(character)
                    break
            # Add calculated value
            print(first_digit , last_digit)
            if first_digit is not None and last_digit is not None:
                result += (first_digit * 10 + last_digit)
    return result

file_path = 'test.txt'
total_coordinates = get_coordinates_from_file(file_path)
print(total_coordinates)
