# This assignment exceeds expectations because I added constants for Earth's 
# acceleration of gravity, water density, and water dynamic viscosity that I 
# then used throughout my program

EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    """This functions calculates and returns the height of a column of water 
    based on the tower height and tank wall height
    return: height of water column in meters
    parameters: height of tower in meters
                height of tank walls in meters"""
    height = tower_height + (3 * tank_height / 4)
    return height

def pressure_gain_from_water_height(height):
    """Calculates are returns pressure caused by Earth's gravity
    return: pressure in kilopascals
    parameter: height of water column in meters"""

    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of friction in the pipe
    return: water pressure lost in kilopascals
    parameters: diameter of the pipe in meters
                length of the pipe in meters
                coefficient of friction
                fluid velocity in meters per second"""
    
    lost_pressure = -(friction_factor * pipe_length * WATER_DENSITY * fluid_velocity * fluid_velocity) / (2000 * pipe_diameter)
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the water pressure lost from fitting bends in the pipeline
    return: water pressure lost in kilopascals
    parameters: fluid velocity in meters per second
                quantity fittings as an integer"""
    lost_pressure = - (0.04 * WATER_DENSITY * fluid_velocity * fluid_velocity * quantity_fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number for a pipe with water flowing through it
    return: Reynolds numbers
    parameters: hydraulic diameter in meters
                fluid velocity in meters per second"""
    reynolds_number = (WATER_DENSITY * hydraulic_diameter * fluid_velocity ) / WATER_DYNAMIC_VISCOSITY
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates the pressure lost from reducing pipe diameters
    returns: pressure lost in kilopascals
    parameters: diameter of larger pipe in meters
                fluid velocity in meters per second
                reynolds number
                diameter of smaller pipe in meters"""
    k_constant = (0.1 + (50 / reynolds_number)) * (((larger_diameter/smaller_diameter) ** 4) - 1)
    lost_pressure = - (k_constant * WATER_DENSITY * fluid_velocity * fluid_velocity) / 2000
    return lost_pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()