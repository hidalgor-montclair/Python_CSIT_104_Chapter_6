import math  # We import the math module to use math functions like square root.

# This function is supposed to get points from the user, but it's not finished yet.
def get_points(num_points):
    """Get num points from the user. Return a list of (x, y) tuples."""
    # This is a placeholder for the function. "NotImplementedError" is raised to stop the program here.
    raise NotImplementedError  # This tells the program to stop because the function isn't finished.

# This function calculates the distance (or length) between two points (p1 and p2).
# It uses the distance formula: √((x2 - x1)^2 + (y2 - y1)^2)
def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# This function calculates the perimeter of a triangle given its points.
def get_perimeter_length(points):
    # First, we calculate the distance between the three sides of the triangle
    perimeter = side_length(points[0], points[1])  # Side 1
    perimeter += side_length(points[0], points[2])  # Side 2
    perimeter += side_length(points[1], points[2])  # Side 3
    return perimeter  # Return the total perimeter

# This part of the program calls the function to get points, then calculates and prints the perimeter.
coordinates = get_points(3)  # We are supposed to get 3 points for the triangle, but this will raise an error.
print(f'Perimeter of triangle: {get_perimeter_length(coordinates)}')  # This line won't be reached because of the error.
