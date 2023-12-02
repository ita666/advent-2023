import os


def check_valid_game(input_string):
    colours_check = { "red":0, "green":0, "blue":0 }
    colours = ["red", "green", "blue"]

    input_string = input_string.replace(',','')
    clean_input = input_string.split(':')

    if len(clean_input) > 1:
        my_throw = clean_input[1].split(';')
        for throw in my_throw:
            #print(throw)
            throwx = throw.strip().split()
            for colour in colours:
                if colour in throwx:
                    colour_index = throwx.index(colour)
                    if colour_index - 1 >= 0 and throwx[colour_index - 1].isdigit() and int(throwx[colour_index -1]) > colours_check[colour]:
                        colours_check[colour] = int(throwx[colour_index -1])
    
    if colours_check["red"] <= 12 and colours_check["green"]  <= 13 and colours_check["blue"] <=14:
        return True
    else:
        return False

def get_gameNumber(input_string):
    clean_input = input_string.split(':')
    game_string = clean_input[0].split()
    return int(game_string[1])

def get_numberOfGame(file_path):
    #Check that the file exists
    if not os.path.exists:
        print(f"file does not exist: {file_path}")
        return 0
    
    result = 0

    with open(file_path,'r') as file:
        for input_string in file:
            if check_valid_game(input_string):
                result += get_gameNumber(input_string)
    return result


file_path = "game.txt"
print(get_numberOfGame(file_path))