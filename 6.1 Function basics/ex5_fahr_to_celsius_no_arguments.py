def fahr1_to_celsius_no_args():
    # Here, we use constant values inside the function
    temp = 32  # We're setting the temperature in Fahrenheit as a constant
    constant1 = 32  # Constant used to subtract from Fahrenheit temperature
    constant2 = 5/9  # The constant used to convert the temperature
    return (temp - constant1) * constant2

# Calling the function with NO arguments
# The function will always convert 32°F (freezing point) to Celsius
freezing_point_celsius = fahr1_to_celsius_no_args()
print("Freezing point of water (no args):", freezing_point_celsius, "°C")  # Output: 0.0 °C


def fahr2_to_celsius_no_args():
    # Here, we use constant values inside the function
    temp = 212  # We're setting the temperature in Fahrenheit as a constant
    constant1 = 32  # Constant used to subtract from Fahrenheit temperature
    constant2 = 5/9  # The constant used to convert the temperature
    return (temp - constant1) * constant2

# Calling the function with NO arguments
# The function will always convert 212°F (freezing point) to Celsius
freezing_point_celsius = fahr2_to_celsius_no_args()
print("Freezing point of water (no args):", freezing_point_celsius, "°C")  # Output: 100.0 °C