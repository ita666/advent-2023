import os


def convert_string_l(input_string):
    number_map = {
        "Threeight":'3', "eighthree":'8',"twone":'2',"oneight":"1","eightwo":'8',"nineight" :'9', "fiveight":'5' ,"one":'1',"eight":'8', "two":'2', "three":'3', "five":'5', "nine":'9', "four":'4', "six":'6', "seven":'7'
    }
    #check for long string first to be sure to avoid partial conversion
    for key in number_map.keys():
        #print(key)
        input_string = input_string.replace(key, number_map[key])
    return input_string


def convert_string_r(input_string):
    number_map = {
        "Threeight":'8', "eighthree":'3',"twone":'1',"oneight":"8","eightwo":'2',"nineight" :'8', "fiveight":'8' , "two":'2', "eight":'8', "three":'3', "nine":'9', "seven":'7', "six":'6', "four":'4', "five":'5', "one":'1'
    }
    #check for long string first to be sure to avoid partial conversion
    for key in number_map.keys():
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
            convertl = input_string
            convertl = convert_string_l(convertl)
            # Find the first digit
            for character in convertl:
                if character.isdigit():
                    first_digit = int(character)
                    break
            # Find the last digit
            convertr = input_string
            convertr = convert_string_r(convertr)
            for character in reversed(convertr.strip()):
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
