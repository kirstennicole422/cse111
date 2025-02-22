import csv
import math

GRAVATATIONAL_ACCELERATION = 9.8066500

def distance_converter(value, distance_unit):
    """Takes distance value and returns in meters
    Parameters: distance
                units
    Return: value in meters"""
    if distance_unit == "mi":
        value *= 1609.344
    elif distance_unit == "yd":
        value *= 0.9144
    elif distance_unit == "ft":
        value *= 0.3048
    elif distance_unit == "in":
        value *= 0.0254
    elif distance_unit == "km":
        value *= 1000
    elif distance_unit == "hm":
        value *= 100
    elif distance_unit == "dam":
        value *= 10
    elif distance_unit == "dm":
        value *= 0.1
    elif distance_unit == "cm":
        value *= 0.01
    elif distance_unit == "mm":
        value *= 0.001
    return value

def time_converter(value, time_unit):
    """Takes time value and returns in seconds
    Parameters: time
                units
    Return: time in seconds"""
    if time_unit == "yr":
        value *= 3.154 * (10 ** 7) 
    elif time_unit == "mo":
        value *= 2.628 * (10 ** 6) 
    elif time_unit == "wk":
        value *= 604800 
    elif time_unit == "d":
        value *= 86400
    elif time_unit == "hr":
        value *= 3600
    elif time_unit== "min":
        value *= 60      
    elif time_unit == "ms":
        value /= 1000
    return value

def unit_splitter(unit_list):
    """Takes the unit list and splits each item into a list composed of its
    parts. m/s/s becomes [m], [s], [s]
    Parameters: unit list
    Return: split unit list in the form of a complex list"""
    unit_split = []
    unit_split_row = []
    for row in unit_list:
        for unit in row:
            unit_split_row.append(unit.split("/"))
        unit_split.append(unit_split_row)
        unit_split_row = []
    return unit_split

def unit_converter(value, units):
    """Determines which converter function(s) to make the value's units meters 
    and seconds and calls them
    Parameters: value
                distance units
                time unit 1
                time unit 2
    Return: value in m/s"""
    for i in range (len(units)):
        if type(value[i]) is float:
            if len(units[i]) == 1:
                unit = units[i][0].lower()
                if unit == "yd" or unit == "ft" or unit == "in" or unit == "km" or unit == "hm" or unit == "dam" or unit == "dm" or unit == "cm" or unit == "mm":
                    value[i] = distance_converter(value[i], units[i][0])
                if unit == "yr" or unit == "mo" or unit  == "wk" or unit == "d" or unit == "hr" or unit == "min" or unit  == "ms":
                    value[i] = time_converter(value[i], units[i][0])

            elif len(units[i]) == 2:
                value[i] = distance_converter(value[i], units[i][0])
                value[i] = distance_converter(value[i], units[i][1])

            elif len(units[i]) == 3:
                value[i] = distance_converter(value[i], units[i][0])
                value[i] = time_converter(value[i], units[i][1])
                value[i] = time_converter(value[i], units[i][2])    

    return value

def convert_digit_to_float(value):
    """Checks if input string can be converted to a float, is the gravatational
    constant, or must remain a string
    Parameters: value as string
    Return: value as float is numeric, gravatational constant if "g", or a 
            string otherwise"""
    try:
        value = float(value)
    except:
        if value.lower() == "g":
            value = GRAVATATIONAL_ACCELERATION
        
    return value

def print_header(distance, velocity_initial, velocity_final, acceleration, time):
    """Determines what values were given and prints the beginning of the sentence that will display the values
    Parameters: distance
                initial velocity
                final velocity
                acceleration
                time
    Return: none, just prints"""

    print(f"For", end="")
    if type(distance) is float:
        print(f" a distance of {distance:4f} meters,", end="")
    if type(velocity_initial) is float:
        print(f" an initial velocity of {velocity_initial:.4f} meters/second,", end="")
    if type(velocity_final) is float and type(acceleration) is not float and type(time) is not float:
        print(f" and a final velocity of {velocity_final:.4f} meters/second", end="")
    elif type(velocity_final) is float:
        print(f" a final velocity of {velocity_final:.4f} meters/second,", end="")
    if type(acceleration) is float and type(time) is not float:
        print(f" and an acceleration of {acceleration:.4f} meters/second/second", end="")
    elif type(acceleration) is float:
        print(f" an acceleration of {acceleration} meters/second/second,", end="")
    if type(time) is float:
        print(f" and a time of {time:.4f} seconds", end="")
    print(":")

def determine_missing_variable(distance, velocity_initial, velocity_final, acceleration, time):
    """Determines which function to call and calls it based on what value is to
    be solved for
    Parameters: distance (m)
                initial velocity (m/s)
                final velocity (m/s)
                acceleration (m/s/s)
                time (s)               
    Return: value from function call"""

    if type(distance) is float and type(velocity_initial) is float and type(velocity_final) is float and type(acceleration) is float and type(time) is float:
        print("There are no values to solve for")

    while not(type(distance) is float and type(velocity_initial) is float and type(velocity_final) is float and type(acceleration) is float and type(time) is float):
        if type(distance) is not float:
            distance = calculate_distance(velocity_initial, velocity_final, acceleration, time)

        if type (velocity_initial) is not float:
            velocity_initial = calculate_velocity_initial(distance, velocity_final, acceleration, time)

        if type(velocity_final) is not float:
            velocity_final = calculate_velocity_final(distance, velocity_initial, acceleration, time)

        if type(acceleration) is not float:
            acceleration = calculate_acceleration(distance, velocity_initial, velocity_final, time)

        if type(time) is not float:
            time = calculate_time(distance, velocity_initial, velocity_final, acceleration)

        print("")

def calculate_distance(velocity_initial, velocity_final, acceleration, time):
    """Determines which distance function to use and prints and returns distance
    Parameters: initial velocity (m/s)
                final velocity (m/s)
                acceleration (m/s/s)
                time (s) 
    Return: distance (m) """
    distance = 0
    if type(velocity_final) is float and type(velocity_initial) is float and type(time) is float:
        distance = (velocity_final + velocity_initial) * time / 2
    
    elif type(velocity_initial) is float and type(time) is float and type(acceleration) is float:        
        distance = (velocity_initial * time) + (acceleration * time * time / 2)

    elif type(velocity_final) is float and type(velocity_initial) is float and type(acceleration) is float:
        distance = ((velocity_final ** 2) - (velocity_initial **2)) / (2 * acceleration)

    else:
        distance = "?"

    if distance != "?":
        print(f"The distance is {distance:.4f} meters")
    return distance

def calculate_velocity_initial(distance, velocity_final, acceleration, time):
    """Determines which initial velocity function to use and returns initial
    velocity
    Parameters: distance (m)
                initial velocity (m/s)
                final velocity (m/s)
                acceleration (m/s/s)
                time (s) 
    Return: initial velocity (m/s)"""
    velocity_initial = 0

    if type(velocity_final) is float and type(acceleration) is float and type(time) is float:    
        velocity_initial = velocity_final - (acceleration * time)

    elif type(velocity_final) is float and type(acceleration) is float and type(distance) is float:
        velocity_initial = math.sqrt((velocity_final * velocity_final) - ( 2 * acceleration * distance))

    elif type(distance) is float and type(time) is float and type(velocity_final) is float:
        velocity_initial = (2 * distance / time) - velocity_final

    elif type(acceleration) is float and type(time) is float and type(distance) is float:
        velocity_initial = (((acceleration * time * time) / 2) - distance) / time

    else:
        velocity_initial = "?"

    if velocity_initial != "?":
        print(f"The initial velocity is {velocity_initial:.4f} meters/second")
    
    return velocity_initial

def calculate_velocity_final(distance, velocity_initial, acceleration, time):
    """Determines which final velocity function to use and returns final velocity
    Parameters: distance (m)
                initial velocity (m/s)
                final velocity (m/s)
                acceleration (m/s/s)
                time (s) 
    Return: final velocity (m/s) """
    velocity_final = 0
    if type(velocity_initial) is float and type(acceleration) is float and type(time) is float:
        velocity_final = velocity_initial + (acceleration * time)
    
    elif type(velocity_initial) is float and type(acceleration) is float and type(distance) is float:
        velocity_final = math.sqrt((velocity_initial * velocity_initial) + ( 2 * acceleration * distance))
    
    elif type(distance) is float and type(time) is float and type(velocity_initial) is float:
        velocity_final = (2 * distance / time) - velocity_initial

    else:
        velocity_final = "?"

    if velocity_final != "?":
        print(f"The final velocity is {velocity_final:.4f} meters/second")
   
    return velocity_final

def calculate_acceleration(distance, velocity_initial, velocity_final, time):
    """Determines which acceleration to use and returns acceleration
    Parameters: distance (m)
                initial velocity (m/s)
                final velocity (m/s)
                time (s) 
    Return: acceleration (m/s/s) """
    acceleration = 0
    if type(velocity_final) is float and type(velocity_initial ) is float and type(time) is float:
        acceleration = (velocity_final - velocity_initial) / time
    
    elif type(distance) is float and type(velocity_initial) is float and type(time) is float:
        acceleration = (2 * ( distance - (velocity_initial * time))) / (time * time)
    
    elif type(velocity_final) is float and type(velocity_initial) is float and type(distance) is float:
        acceleration = ((velocity_final * velocity_final) - (velocity_initial * velocity_initial)) / (2 * distance)

    else:
        acceleration = "?"
    
    if acceleration != "?":
        print(f"The acceleration is {acceleration:.4f} meters/second/second")
    
    return acceleration

def calculate_time(distance, velocity_initial, velocity_final, acceleration):
    """Determines which time function to use and returns time
    Parameters: distance (m)
                initial velocity (m/s)
                final velocity (m/s)
                acceleration (m/s/s)
    Return: time (s) """
    time = 0

    if type(velocity_final) is float and type(velocity_initial) is float and type(acceleration) is float:
        time = (velocity_final - velocity_initial) / acceleration
    
    elif type(distance) is float and type(velocity_final) is float and type(velocity_initial) is float:
        time = (2 * distance) / ( velocity_final + velocity_initial)

    else:
        time = "?"

    if time != "?":
        print(f"The time is {time:4f} seconds")
    
    return time

def file_to_list(data_list, unit_list):
    """Reads and appends data csv to two compound lists: values and units
    Parameters: data list
                unit list
    Return: none but updates paramaters with pass by value"""
    file_data = []
    data_list_line = []
    unit_list_line = []
    with open ("physics_data.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            file_data.append(row_list)
            data_list_line = []

        for line in file_data:
            for item in range(len(line)):
                if item % 2 == 0:
                    data_list_line.append(line[item])
                if item % 2 == 1:
                    unit_list_line.append(line[item])
            data_list.append(data_list_line)
            data_list_line = []
            unit_list.append(unit_list_line)
            unit_list_line = []

def main():
    data_list = []
    unit_list = []
    file_data=[]
    file_to_list(data_list, unit_list)

    for row in data_list:
        for value in row:
            row[row.index(value)] = convert_digit_to_float(value)

    split_unit_list = unit_splitter(unit_list)

    for i in range(len(split_unit_list)):
        data_list[i] = unit_converter(data_list[i], split_unit_list[i])

    for line in data_list:
        distance = line[0]
        velocity_initial = line[1]
        velocity_final = line[2]
        acceleration = line[3]
        time = line[4]

        print_header(distance, velocity_initial, velocity_final, acceleration, time)
        determine_missing_variable(distance, velocity_initial, velocity_final, acceleration, time)

if __name__ == "__main__":
    main()