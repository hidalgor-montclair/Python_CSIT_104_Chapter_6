# This function prints a simple face made from characters.
def print_face():
    print("  o   o  ")  # The eyes
    print("    >    ")  # The nose
    print("  -----  ")  # The mouth

# Here we are calling the print_face() function directly.
print_face()  # This prints the face to the screen.


print()
print()
print()
# Now we assign the function print_face to a new name called func.
# This means that both print_face and func now refer to the same function.
func = print_face

# Calling func() is the same as calling print_face().
# Even though we are using a new name (func), it still does the same thing.
func()  # This also prints the face to the screen.
