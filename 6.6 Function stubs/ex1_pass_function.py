# This function converts the number of steps walked into feet
def steps_to_feet(num_steps):
    # Assume each step is 3 feet
    feet_per_step = 3
    # Multiply the number of steps by feet per step to get total feet
    feet = num_steps * feet_per_step
    # Return the result (the total number of feet)
    return feet

# This function is supposed to convert steps into calories, 
# but right now it doesn't do anything.
# The 'pass' statement is a placeholder meaning "do nothing for now."
def steps_to_calories(num_steps):
    pass  # The function is not yet complete, so it does nothing for now

# Ask the user for the number of steps they've walked
steps = int(input('Enter number of steps walked: '))

# Call the steps_to_feet function to convert steps to feet
feet = steps_to_feet(steps)
# Print the number of feet the user walked
print(f'Feet: {feet}')

# Call the steps_to_calories function to convert steps to calories
calories = steps_to_calories(steps)
# Print the number of calories burned (right now it will show "None" since the function isn't complete)
print(f'Calories: {calories}')
