# This function converts the number of steps walked into feet
def steps_to_feet(num_steps):
    # Assume each step is 3 feet
    feet_per_step = 3
    # Multiply the number of steps by feet per step to get total feet
    feet = num_steps * feet_per_step
    # Return the result (the total number of feet)
    return feet



# This function is supposed to calculate how many calories are burned by walking steps.
# However, the function is not finished yet. 
# The print statement reminds us to finish writing the function later.
def steps_to_calories(steps):
    # This print statement is like a "note to self" for the programmer.
    print('FIXME: finish steps_to_calories')  # "FIXME" means something needs to be fixed or completed
    # Return -1 for now, since the function doesn't calculate anything yet.
    return -1



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
