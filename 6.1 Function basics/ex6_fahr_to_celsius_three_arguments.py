# Function that converts Fahrenheit to Celsius WITH three arguments
def fahr_to_celsius_with_args(temp, constant1, constant2):
    # Here, the temperature and constants are passed as arguments
    return (temp - constant1) * constant2

# Now, we can input custom values when calling the function
# Example 1: Convert freezing point (32°F) using the arguments
freezing_point_celsius = fahr_to_celsius_with_args(32, 32, 5/9)
print("Freezing point of water (with args):", freezing_point_celsius, "°C")  # Output: 0.0 °C

# Example 2: Convert boiling point (212°F) using the arguments
boiling_point_celsius = fahr_to_celsius_with_args(212, 32, 5/9)
print("Boiling point of water (with args):", boiling_point_celsius, "°C")  # Output: 100.0 °C