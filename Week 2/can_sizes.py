import math

def compute_volume(radius, height):
    ''' Takes the radius and height of a cylinder and returns the volume
    Return: volume as a float
    Parameters: radius: radius of cylinder base
                height: height of cylinder'''
    return math.pi * radius * radius * height

def compute_surface_area(radius, height):
    ''' Takes the radius and height of a cylinder and returns the surface area
    Return: surface area as a float
    Parameters: radius: radius of cylinder base
                height: height of cylinder'''
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
    ''' Takes the radius and height of a cylinder and calls the volume and surface area functions to compute storage efficiency
    Return: storage efficiency as float
    Parameters: radius: radius of cylinder base
                height: height of cylinder'''
    return compute_volume(radius, height)/compute_surface_area(radius, height)

def main(size, radius, height, cost):
    '''Takes the size, radius, and height of a cylinder, calls the storage efficiency function and displays the result
    Return: none (text display)
    Parameters: radius: radius of cylinder base
                height: height of cylinder
                size: name of can size'''
    print(f" {size} {compute_storage_efficiency(radius, height):.2f}")

main ("#1 Picnic", 6.83, 10.16, 0.28,)
main ("#1 Tall",	7.78,	11.91,	0.43)
main ("#2",	8.73,	11.59,	0.45)
main ("#2.5",	10.32,	11.91,	0.61)
main ("#3 Cylinder",	10.79,	17.78,	0.86)
main ("#5",	13.02,	14.29,	0.83)
main ("#6Z",	5.40,	8.89,	0.22)
main ("#8Z short",	6.83,	7.62,	0.26)
main ("#10",	15.72,	17.78,	1.53)
main ("#211",	6.83,	12.38,	0.34)
main ("#300",	7.62,	11.27,	0.38)
main ("#303",	8.10,	11.11,	0.42)
