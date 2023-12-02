import os


def get_game_power(input_string):
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
    
    return colours_check["red"] * colours_check["green"] * colours_check["blue"]


def get_numberOfGame(file_path):
    #Check that the file exists
    if not os.path.exists:
        print(f"file does not exist: {file_path}")
        return 0
    
    result = 0

    with open(file_path,'r') as file:
        for input_string in file:
            result += get_game_power(input_string)
    return result


file_path = "game.txt"
print(get_numberOfGame(file_path))