#d = ut + 1/2 * at^2
#u initial velocity at 0 seconds
#a acceleration a 1mm/ms2
#1/2 * t^2
#d = 1/2 * (racetime - x)^2

def get_races(pathFile):
    with open(pathFile) as file:
        lines = file.readlines()
    time_data = lines[0].split()[1:]  
    time_data = [int(time) for time in time_data] 

    distance_data = lines[1].split()[1:] 
    distance_data = [int(distance) for distance in distance_data]

    races = list(zip(time_data, distance_data))
    return races

def calculate_distance(hold_time, total_time):
    speed = hold_time  
    travel_time = total_time - hold_time  
    return speed * travel_time  


def getBestDistance(races):
    ways_to_win = []
    for race_time, record_distance in races:
        ways = 0
        for hold_time in range(race_time + 1):
            #print("Hold time:", hold_time)
            #print(calculate_distance(hold_time, race_time))
            if calculate_distance(hold_time, race_time) > record_distance:
                ways += 1
        ways_to_win.append(ways)
    return ways_to_win

races = get_races("boat.txt")
ways_to_win = getBestDistance(races)

total_ways = 1
for ways in ways_to_win:
    #print ("Ways to win:", ways)
    total_ways *= ways

print("Total ways to win across all races:", total_ways)


