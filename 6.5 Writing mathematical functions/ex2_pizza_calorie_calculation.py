# This function calculates the area of a circle.
# We need to know the diameter of the circle to calculate the area.
def calc_circle_area(circle_diameter):

    print()
    print("circle_diameter is invoked")
    print()


    pi_val = 3.14159265  # The value of Pi (π) for the calculation
    circle_radius = circle_diameter / 2.0  # The radius is half the diameter
    # The formula for the area of a circle is π * r^2 (where r is the radius)
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area  # Return the calculated area

# This function calculates the number of calories in a pizza.
# We need to know the diameter of the pizza to do this.
def calc_pizza_calories(pizza_diameter):

    print()
    print("calc_pizza_calories is invoked")
    print()


    calories_per_square_inch = 16.7  # There are 16.7 calories per square inch of pizza
    # First, calculate the area of the pizza using the calc_circle_area function
    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories  # Return the total calories

# Print the number of calories in a 12-inch pizza.
# We call the calc_pizza_calories function with a pizza diameter of 12 inches.
print(f'12 inch pizza has {calc_pizza_calories(12.0):.2f} calories.')

# Print the number of calories in a 14-inch pizza.
# We call the calc_pizza_calories function with a pizza diameter of 14 inches.
print(f'14 inch pizza has {calc_pizza_calories(14.0):.2f} calories.')
