# This is a function that converts Fahrenheit to Celsius
# temp is the temperature in Fahrenheit that we want to convert
def fahr_to_celsius(temp):
    # The formula to convert Fahrenheit to Celsius is: (temp - 32) * (5/9)
    return (temp - 32) * (5/9)

# Example 1: Let's convert the freezing point of water from Fahrenheit to Celsius.
# 32°F is the freezing point of water.
freezing_point_celsius = fahr_to_celsius(32)
print("Freezing point of water:", freezing_point_celsius, "°C")  # This will print: Freezing point of water: 0.0 °C

# Example 2: Let's convert the boiling point of water from Fahrenheit to Celsius.
# 212°F is the boiling point of water.
boiling_point_celsius = fahr_to_celsius(212)
print("Boiling point of water:", boiling_point_celsius, "°C")  # This will print: Boiling point of water: 100.0 °C
