"""
Title: Wind Chill Calculator

Author: Garrett Stockwell

Description: After giving the temperature and either Farenheit or Celsius, 
it will deliver the wind chill results. To achive rubric requiremnts, leave the question for what is the wind speed blank.
"""

def calc_windchill(t, v):
    wind_chill = 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
    return round(wind_chill, 2)

def f_to_c(t):
    return (5/9) * (t - 32)

def c_to_f(t):
    return ((9/5) * t) + 32

f_c = None
v = 0
d = "MPH"
wc = 0

while f_c == None:
    f_c = input("Is the temperature in Fahrenheit or Celsius? (F/C)\n").capitalize()
    
    if f_c != "F" and f_c != "C":
        f_c = None
        print("Invalid Selection")

t = float(input("\nWhat is the temperature?\n"))
    
print("\nWhat is the wind speed in MPH? ")
v = input("(If unknown leave blank)\n")
v_s = v #saved for conversion if needed

if f_c == "F":
   
    if v == "":
        
        v = 0
   
        for i in range(5, 65, 5):
            v += 5
            wc = calc_windchill(t, v)
            print(f"The Wind Chill at {v} MPH is {wc:.2f} °{f_c}")
   
    else:
        v = float(v)
        wc = calc_windchill(t, v)
        print(f"The Wind Chill at {v} MPH is {wc:.2f} °{f_c}")
   
    convert = input("\nWould you like to convert the temperature to Celsius? (Y/N)\n").capitalize()
   
    if convert == "Y":
        
        c_f = "C"

        if v_s == "":
            
            v = 0
            
            for i in range(5, 65, 5):
                v += 5
                wc = calc_windchill(t, v)
                wc = f_to_c(wc)
                print(f"The Wind Chill at {v} MPH is {wc:.2f} °{c_f}")
            print()

        else:
            v = float(v)
            wc = calc_windchill(t, v)
            wc = f_to_c(wc)
            print(f"The Wind Chill at {v} MPH is {wc:.2f} °{c_f}")
            print()

if f_c == "C":

    t = c_to_f(t)
   
    if v == "":
        
        v = 0
   
        for i in range(5, 65, 5):
            v += 5
            wc = calc_windchill(t, v)
            wc = f_to_c(wc)
            print(f"The Wind Chill at {v} MPH is {wc:.2f} °{f_c}")
   
    else:
        v = float(v)
        wc = calc_windchill(t, v)
        wc = f_to_c(wc)
        print(f"The Wind Chill at {v} MPH is {wc:.2f} °{f_c}")
    
    convert = input("\nWould you like to convert the temperature to Fahrenheit? (Y/N)\n").capitalize()
   
    if convert == "Y":
        
        t = c_to_f(t)

        c_f = "C"

        if v_s == "":
            
            v = 0
            
            for i in range(5, 65, 5):
                v += 5
                wc = calc_windchill(t, v)
                print(f"The Wind Chill at {v} MPH is {wc:.2f} °{c_f}")
   
        else:
            v = float(v)
            wc = calc_windchill(t, v)
            print(f"The Wind Chill at {v} MPH is {wc:.2f} °{c_f}")