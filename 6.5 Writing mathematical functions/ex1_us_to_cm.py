# This is the number of centimeters in one inch
CM_PER_INCH = 2.54

# This is the number of inches in one foot
INCHES_PER_FOOT = 12

# This function converts height from feet and inches to centimeters
def height_US_to_cm(feet, inches):
    """Converts height in feet and inches to centimeters"""
    # Calculate the total number of inches (feet converted to inches + extra inches)
    total_inches = feet * INCHES_PER_FOOT + inches
    # Convert the total inches to centimeters
    cm = total_inches * CM_PER_INCH
    # Return the result in centimeters
    return cm

# Example height: 6 feet 4 inches
feet = 6  # The number of feet
inches = 4  # The number of extra inches

# Call the function to convert the height to centimeters
centimeters = height_US_to_cm(feet, inches)

# Print the result
print(f'Centimeters: {centimeters}')
